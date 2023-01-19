import inspect
import warnings
from typing import Type

from otlmow_model.BaseClasses.RelationInteractor import RelationInteractor
from otlmow_model.Classes.ImplementatieElement.RelatieObject import RelatieObject
from otlmow_model.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning


class RelationValidator:
    @staticmethod
    def is_valid_relation_instance(source: RelationInteractor, relation_instance: RelatieObject, 
                                   target: RelationInteractor) -> bool:
        """
        Verifies if a relation would be valid between a source and a target, given the instance of that relation

        :param source: the intended source for the relation
        :param relation_instance: the instance of the relation
        :param target: the intended source for the relation
        :return: 'True' if the relation would be valid, 'False' otherwise
        """
        return RelationValidator.is_valid_relation(source=source, target=target,
                                                   relation_type=type(relation_instance))

    @staticmethod
    def is_valid_relation(source: RelationInteractor, relation_type: Type[RelatieObject],
                          target: RelationInteractor) -> bool:
        """
        Verifies if a relation would be valid between a source and a target, given a relation_type type

        :param source: the intended source for the relation_type
        :param relation_type: the intended type of the relation
        :param target: the intended source for the relation_type
        :return: 'True' if the relation would be valid, 'False' otherwise
        """
        if 'lgc.' in source.typeURI or 'lgc.' in target.typeURI:
            return True

        if relation_type.typeURI not in source._valid_relations:
            return False

        targets = source._valid_relations[relation_type.typeURI].keys()
        if target.typeURI in targets:
            deprecated_value = source._valid_relations[relation_type.typeURI][target.typeURI]
            if deprecated_value != '':
                warnings.warn(
                    message=f'the relation_type of type {relation_type.typeURI} between assets of types '
                            f'{source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                    category=RelationDeprecationWarning)
            return True

        bases = inspect.getmro(type(target))
        for base in bases:
            base_type_uri = RelationValidator._get_member(base, 'typeURI')
            if base_type_uri in targets:
                deprecated_value = source._valid_relations[relation_type.typeURI][base_type_uri]
                if deprecated_value != '':
                    warnings.warn(
                        message=f'the relation_type of type {relation_type.typeURI} between assets of types '
                                f'{source.typeURI} and {target.typeURI} is deprecated since version {deprecated_value}',
                        category=RelationDeprecationWarning)
                return True

        return False

    @staticmethod
    def _get_member(obj, name):
        return next(iter([member for _name, member in inspect.getmembers(obj) if name == _name]), None)
