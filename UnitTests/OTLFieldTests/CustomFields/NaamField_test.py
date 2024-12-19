import pytest
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.Classes.ImplementatieElement.AIMNaamObject import NaamField


class NaamClass:
    def __init__(self):
        super().__init__()

        self._naam = OTLAttribuut(field=NaamField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
                                  definition='De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.',
                                  owner=self)

    @property
    def naam(self) -> str:
        """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)


@pytest.mark.parametrize("value, expected, id", [
    ("validName123", True, "valid_alphanumeric"),
    ("valid.name-123", True, "valid_with_special_chars"),
    ("", True, "empty_string"),
    ("a", True, "single_character"),
    ("invalid name!", False, "invalid_with_space_and_exclamation"),
    ("invalid@name", False, "invalid_with_at_symbol")])
def test_validate(value, expected, id):
    result = NaamField.validate(value, NaamClass()._naam)
    assert result == expected, f"Test case '{id}' failed: expected {expected} but got {result}"
