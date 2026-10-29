import inspect
import warnings
from pathlib import Path
from typing import Type

from ..BaseClasses.OTLObject import dynamic_create_instance_from_uri
from ..BaseClasses.RelationInteractor import RelationInteractor
from ..Classes.ImplementatieElement.RelatieObject import RelatieObject
from ..Exceptions.RelationDeprecationWarning import RelationDeprecationWarning


def is_valid_relation_instance(
    source: RelationInteractor,
    relation_instance: RelatieObject,
    target: RelationInteractor,
    model_directory: Path = None,
) -> bool:
    """
    Verifies if a relation would be valid between a source and a target, given the instance of that relation

    :param source: the intended source for the relation
    :type: RelationInteractor
    :param relation_instance: the instance of the relation
    :type: RelatieObject
    :param target: the intended target for the relation
    :type: RelationInteractor
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: 'True' if the relation would be valid, 'False' otherwise
    """
    return is_valid_relation(
        source=source, target=target, relation_type=type(relation_instance), model_directory=model_directory
    )


def is_valid_relation_using_relation_uri(
    relation_uri: str,
    source: RelationInteractor | None = None,
    source_typeURI: str | None = None,
    target: RelationInteractor | None = None,
    target_typeURI: str | None = None,
    model_directory: Path = None,
) -> bool:
    """
    Verifies if a relation would be valid between a source and a target, given a relation_type type. Exactly one of
    source or source_typeURI must not be None. Exactly one of target or target_typeURI must not be None.

    :param relation_type: the intended type of the relation
    :param source: the intended source for the relation_type
    :type: RelationInteractor
    :param source_typeURI: the typeURI of the intended source for the relation
    :type: str
    :param target: the intended source for the relation
    :type: RelationInteractor
    :param target_typeURI: the typeURI of the intended target for the relation
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: 'True' if the relation would be valid, 'False' otherwise
    """

    source, source_typeURI = _override_actor(source, source_typeURI, 'source', model_directory)
    target, target_typeURI = _override_actor(target, target_typeURI, 'target', model_directory)

    source_typeURI = _require_type_uri(source, source_typeURI, 'source')
    target_typeURI = _require_type_uri(target, target_typeURI, 'target')

    if _is_legacy(source_typeURI, target_typeURI):
        return True

    if source is None:
        source = dynamic_create_instance_from_uri(class_uri=source_typeURI, model_directory=model_directory)

    valid_relations = source._valid_relations
    if relation_uri not in valid_relations:
        return False

    relation = valid_relations[relation_uri]
    if target_typeURI in relation:
        return _is_allowed_relation(relation[target_typeURI], relation_uri, source_typeURI, target_typeURI)

    if target is None:
        target = dynamic_create_instance_from_uri(class_uri=target_typeURI, model_directory=model_directory)

    return _is_allowed_relation_in_mro(target, relation, relation_uri, source_typeURI, target_typeURI)


def _is_legacy(source_typeURI: str, target_typeURI: str) -> bool:
    return 'lgc.' in source_typeURI or 'lgc.' in target_typeURI


def _is_allowed_relation_in_mro(
    target, relation: dict, relation_uri: str, source_typeURI: str, target_typeURI: str
) -> bool:
    for base in inspect.getmro(type(target)):
        base_type_uri = _get_member(base, 'typeURI')
        if base_type_uri in relation:
            return _is_allowed_relation(relation[base_type_uri], relation_uri, source_typeURI, target_typeURI)
    return False


def _override_actor(
    actor: RelationInteractor | None, actor_typeURI: str | None, name: str, model_directory: Path = None
):
    if actor is not None and actor_typeURI is not None:
        warnings.warn(
            f'both {name} and {name}_typeURI are not None. Overriding {name} by instantiating it', RuntimeWarning
        )
        actor = dynamic_create_instance_from_uri(class_uri=actor_typeURI, model_directory=model_directory)
    return actor, actor_typeURI


def _require_type_uri(actor: RelationInteractor | None, actor_typeURI: str | None, name: str) -> str:
    if actor is not None and actor_typeURI is None:
        actor_typeURI = actor.typeURI
    if actor_typeURI is None:
        raise ValueError(f'Exactly one of {name} or {name}_typeURI needs to be not None.')
    return actor_typeURI


def _is_allowed_relation(entry: dict, relation_uri: str, source_typeURI: str, target_typeURI: str) -> bool:
    if 'i' in entry and 'o' not in entry:
        return False
    deprecated_value = list(entry.values())[0]
    if deprecated_value != '':
        warnings.warn(
            message=f'the relation_type of type {relation_uri} between assets of types '
            f'{source_typeURI} and {target_typeURI} is deprecated since version {deprecated_value}',
            category=RelationDeprecationWarning,
        )
    return True


def is_valid_relation(
    relation_type: Type[RelatieObject],
    source: RelationInteractor | None = None,
    source_typeURI: str | None = None,
    target: RelationInteractor | None = None,
    target_typeURI: str | None = None,
    model_directory: Path = None,
) -> bool:
    """
    Verifies if a relation would be valid between a source and a target, given a relation_type type. Exactly one of
    source or source_typeURI must not be None. Exactly one of target or target_typeURI must not be None.

    :param relation_type: the intended type of the relation
    :param source: the intended source for the relation_type
    :type: RelationInteractor
    :param source_typeURI: the typeURI of the intended source for the relation
    :type: str
    :param target: the intended source for the relation
    :type: RelationInteractor
    :param target_typeURI: the typeURI of the intended target for the relation
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: 'True' if the relation would be valid, 'False' otherwise
    """
    return is_valid_relation_using_relation_uri(
        relation_uri=relation_type.typeURI,
        source=source,
        source_typeURI=source_typeURI,
        target=target,
        target_typeURI=target_typeURI,
        model_directory=model_directory,
    )


def _get_member(obj, name):
    return next(iter([member for _name, member in inspect.getmembers(obj) if name == _name]), None)
