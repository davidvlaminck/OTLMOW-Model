import warnings
from pathlib import Path

from ..BaseClasses.OTLObject import dynamic_create_instance_from_uri
from ..BaseClasses.RelationInteractor import RelationInteractor
from ..Classes.Agent import Agent
from ..Classes.ImplementatieElement.RelatieObject import RelatieObject
from ..Classes.Onderdeel.HeeftBetrokkene import HeeftBetrokkene
from ..Exceptions.CouldNotCreateRelationError import CouldNotCreateRelationError
from ..Helpers.GenericHelper import validate_guid, get_aim_id_from_uuid_and_typeURI
from ..Helpers.RelationValidator import is_valid_relation


def _default_model_directory(model_directory: Path | None) -> Path:
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent
    return model_directory


def _require_exactly_one(name: str, obj: RelationInteractor | None, typeURI: str | None, uuid: str | None) -> None:
    if obj is None and (typeURI is None or uuid is None):
        raise ValueError(f'Exactly one of {name} or ({name}_typeURI + {name}_uuid) needs to be not None.')


def _warn_object_and_type_uri(name: str, obj: RelationInteractor | None, typeURI: str | None) -> None:
    if obj is not None and typeURI is not None:
        warnings.warn(
            f'both {name} and {name}_typeURI are not None. Using {name} and ignoring {name}_type_uri.', RuntimeWarning
        )


def _resolve_aim_id(uuid: str | None, typeURI: str | None) -> tuple[str, bool]:
    if not validate_guid(uuid):
        raise ValueError(f'{uuid} is not a valid guid format.')
    return get_aim_id_from_uuid_and_typeURI(uuid, typeURI), 'lgc.' in typeURI


def _instantiate(typeURI: str, uuid: str | None, model_directory: Path) -> tuple[RelationInteractor, bool, str]:
    aim_id, is_legacy = _resolve_aim_id(uuid, typeURI)
    instance = dynamic_create_instance_from_uri(class_uri=typeURI, model_directory=model_directory)
    if typeURI == 'http://purl.org/dc/terms/Agent':
        instance.agentId.identificator = aim_id
        instance.agentId.toegekendDoor = 'AWV'
    else:
        instance.assetId.identificator = aim_id
        instance.assetId.toegekendDoor = 'AWV'
    return instance, is_legacy, aim_id


def _require_valid_id(instance: RelationInteractor, name: str, is_legacy: bool) -> None:
    if not is_legacy:
        if instance.typeURI == 'http://purl.org/dc/terms/Agent' and instance.agentId.identificator is None:
            raise AttributeError(
                f'In order to create a relation_type, the {name} needs to have a valid agentId '
                f'({name}.agentId.identificator)'
            )
        elif instance.typeURI != 'http://purl.org/dc/terms/Agent' and instance.assetId.identificator is None:
            raise AttributeError(
                f'In order to create a relation_type, the {name} needs to have a valid assetId '
                f'({name}.assetId.identificator)'
            )


def _set_relation_end(
    relation_type: RelatieObject, end: str, aim_id: str, instance: RelationInteractor, typeURI: str, is_legacy: bool
) -> str:
    asset_id_attribute = getattr(relation_type, f'{end}AssetId')
    if is_legacy:
        asset_id_attribute.identificator = aim_id
        asset_id_attribute.toegekendDoor = 'AWV'
        segment = aim_id
        return segment
    actual_typeURI = typeURI if typeURI is not None else getattr(instance, 'typeURI', None)
    if actual_typeURI == 'http://purl.org/dc/terms/Agent':
        asset_id_attribute.identificator = instance.agentId.identificator
        asset_id_attribute.toegekendDoor = instance.agentId.toegekendDoor
        segment = instance.agentId.identificator
    else:
        asset_id_attribute.identificator = instance.assetId.identificator
        asset_id_attribute.toegekendDoor = instance.assetId.toegekendDoor
        segment = instance.assetId.identificator
    return segment


def create_relation(
    relation_type: type[RelatieObject],
    source: RelationInteractor | None = None,
    target: RelationInteractor | None = None,
    source_uuid: str | None = None,
    source_typeURI: str | None = None,
    target_uuid: str | None = None,
    target_typeURI: str | None = None,
    model_directory: Path = None,
) -> RelatieObject | None:
    """
    Instantiates a relation, if valid, between instantiated objects, given a specific relation type.
    Instead of instantiated objects, valid guids and typeURI's can be provided, for source and/or target.

    :param relation_type: the relation type of the relation to be created
    :type: RelatieObject
    :param source: the intended source for the relation
    :type: RelationInteractor
    :param target: the intended target for the relation
    :type: RelationInteractor
    :param source_uuid: the uuid of the intended source for the relation
    :type: str
    :param source_typeURI: the typeURI of the intended source for the relation
    :type: str
    :param target_uuid: the uuid of the intended target for the relation
    :type: str
    :param target_typeURI: the typeURI of the intended target for the relation
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str

    :return: Returns the instantiated relation between the given source and target, or None if the relation is invalid.
    :rtype: RelatieObject or None
    """

    model_directory = _default_model_directory(model_directory)

    _require_exactly_one('source', source, source_typeURI, source_uuid)
    _require_exactly_one('target', target, target_typeURI, target_uuid)

    _warn_object_and_type_uri('source', source, source_typeURI)
    _warn_object_and_type_uri('target', target, target_typeURI)

    source, source_is_legacy, source_aim_id = _resolve_end(source, source_typeURI, source_uuid, model_directory)
    target, target_is_legacy, target_aim_id = _resolve_end(target, target_typeURI, target_uuid, model_directory)

    if not (source_is_legacy or target_is_legacy):
        _require_valid_relation(source, target, relation_type)

    relation_type = dynamic_create_instance_from_uri(class_uri=relation_type.typeURI, model_directory=model_directory)

    _require_valid_id(source, 'source', source_is_legacy)
    _require_valid_id(target, 'target', target_is_legacy)

    bron_segment = _set_relation_end(relation_type, 'bron', source_aim_id, source, source_typeURI, source_is_legacy)
    doel_segment = _set_relation_end(relation_type, 'doel', target_aim_id, target, target_typeURI, target_is_legacy)
    relation_id = relation_type.__class__.__name__ + '_-_' + bron_segment + '_-_' + doel_segment

    relation_type.assetId.identificator = relation_id
    relation_type.assetId.toegekendDoor = 'OTLMOW'

    relation_type.bron.typeURI = source_typeURI if source_is_legacy else source.typeURI
    relation_type.doel.typeURI = target_typeURI if target_is_legacy else target.typeURI

    return relation_type


def _resolve_end(
    obj: RelationInteractor | None, typeURI: str | None, uuid: str | None, model_directory: Path
) -> tuple[RelationInteractor, bool, str | None]:
    """Return the object, whether it is a legacy object and its aim id."""
    is_legacy = obj is None and 'lgc.' in typeURI
    aim_id = None
    if obj is None:
        obj, is_legacy, aim_id = _instantiate(typeURI, uuid, model_directory)
    return obj, is_legacy, aim_id


def _require_valid_relation(
    source: RelationInteractor, target: RelationInteractor, relation_type: type[RelatieObject]
) -> None:
    valid = is_valid_relation(source=source, target=target, relation_type=relation_type)
    if not valid:
        raise CouldNotCreateRelationError("Can't create an invalid relation_type, please validate relations first")


def create_betrokkenerelation(
    rol: str,
    source: RelationInteractor | None = None,
    target: Agent | None = None,
    source_uuid: str | None = None,
    source_typeURI: str | None = None,
    target_uuid: str | None = None,
    target_typeURI: str | None = None,
    model_directory: Path = None,
) -> HeeftBetrokkene | None:
    relation = create_relation(
        source=source,
        target=target,
        source_uuid=source_uuid,
        source_typeURI=source_typeURI,
        target_uuid=target_uuid,
        target_typeURI=target_typeURI,
        model_directory=model_directory,
        relation_type=HeeftBetrokkene,
    )
    relation.rol = rol
    return relation
