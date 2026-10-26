from abc import abstractmethod
from pathlib import Path

from ..Helpers.generated_lists import get_hardcoded_class_dict, get_concrete_subclasses_from_class_dict


class RelationInteractor:
    typeURI = ''
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def add_valid_relation(self, relation: str, target: str, direction: str = 'o', deprecated: str = ''):
        if relation not in self._valid_relations:
            self._valid_relations[relation] = {}
        if target not in self._valid_relations[relation]:
            self._valid_relations[relation][target] = {}
        self._valid_relations[relation][target][direction] = deprecated

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._valid_relations = {}

    def _get_all_concrete_relations(self, model_directory: Path = None):
        class_dict = get_hardcoded_class_dict(model_directory)
        for relation in self._valid_relations:
            for target in self._valid_relations[relation]:
                for direction, deprecated in self._valid_relations[relation][target].items():
                    for concrete_target in self._concrete_targets(target, class_dict, model_directory):
                        relation_tuple = self._relation_tuple(relation, concrete_target, direction, deprecated)
                        if relation_tuple is not None:
                            yield relation_tuple

    def _concrete_targets(self, target, class_dict, model_directory):
        if class_dict[target]['abstract']:
            return get_concrete_subclasses_from_class_dict(target, model_directory=model_directory)
        return [target]

    def _relation_tuple(self, relation, target, direction, deprecated):
        if direction == 'o':
            return self.typeURI, relation, target, '', deprecated
        if direction == 'i':
            return target, relation, self.typeURI, '', deprecated
        if direction == 'u':
            return self.typeURI, relation, target, 'Unspecified', deprecated
        return None
