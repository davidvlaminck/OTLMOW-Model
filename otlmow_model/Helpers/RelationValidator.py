import inspect
import warnings
from typing import Type

from otlmow_model.BaseClasses.RelationInteractor import RelationInteractor
from otlmow_model.Classes.ImplementatieElement.RelatieObject import RelatieObject
from otlmow_model.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning


class RelationValidator:
    @staticmethod
    def is_valid_relation_instance(source: RelationInteractor, relation_instance: RelatieObject, target: RelationInteractor):
        return RelationValidator.is_valid_relation(source=source,
                                                   relation=type(relation_instance),
                                                   target=target)

    @staticmethod
    def is_valid_relation(source: RelationInteractor, relation: Type[RelatieObject], target: RelationInteractor):
        if 'lgc.' in source.typeURI or 'lgc.' in target.typeURI:
            return True

        if relation.typeURI not in source._valid_relations:
            return False
        targets = source._valid_relations[relation.typeURI].keys()
        if target.typeURI in targets:
            deprecated_value = source._valid_relations[relation.typeURI][target.typeURI]
            if deprecated_value != '':
                warnings.warn(
                    message=f'the relation of type {relation.typeURI} between assets of types {source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                    category=RelationDeprecationWarning)
            return True

        bases = inspect.getmro(type(target))
        for base in bases:
            base_type_uri = RelationValidator._get_member(base, 'typeURI')
            if base_type_uri in targets:
                deprecated_value = source._valid_relations[relation.typeURI][base_type_uri]
                if deprecated_value != '':
                    warnings.warn(
                        message=f'the relation of type {relation.typeURI} between assets of types {source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                        category=RelationDeprecationWarning)
                return True

        # print(bases)
        return False

    @staticmethod
    def _get_member(obj, name):
        return next(iter([member for _name, member in inspect.getmembers(obj) if name == _name]), None)
