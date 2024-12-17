import pytest
import re
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut

from otlmow_model.OtlmowModel.Classes.ImplementatieElement.AIMNaamObject import NaamField

class NaampadField(NaamField):
    def __init__(self, naam: str, label: str, objectUri: str, definition: str, owner):
        super().__init__(naam, label, objectUri, definition, owner)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        return re.match('^[[a-zA-Z0-9.\\-_]*/]*[a-zA-Z0-9.\\-_]*$', value) is not None


class NaampadClass:
    def __init__(self):
        super().__init__()

        self._naam = OTLAttribuut(field=NaamField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
                                  definition='De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.',
                                  owner=self)

        self._naampad = OTLAttribuut(field=NaampadField,
                                     naam='naampad',
                                     label='naampad',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement'
                                               '#AIMNaamObject.naampad',
                                     definition='De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.',
                                     owner=self)

    @property
    def naam(self) -> str:
        """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def naampad(self) -> str:
        """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""
        return self._naampad.get_waarde()

    @naampad.setter
    def naampad(self, value):
        self._naampad.set_waarde(value, owner=self)

def test_naampad_assign():
    naampad_object = NaampadClass()
    naampad_object.naampad = "valid/naampad/123"
    assert naampad_object.naampad == "valid/naampad/123"
    naampad_object.naam = "123"

