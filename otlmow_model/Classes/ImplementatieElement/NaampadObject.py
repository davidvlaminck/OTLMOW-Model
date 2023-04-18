# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class NaampadObject(AIMNaamObject):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._naampad = OTLAttribuut(field=StringField,
                                     naam='naampad',
                                     label='naampad',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                                     definition='Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).',
                                     owner=self)

    @property
    def naampad(self) -> str:
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""
        return self._naampad.get_waarde()

    @naampad.setter
    def naampad(self, value):
        self._naampad.set_waarde(value, owner=self)
