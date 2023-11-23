# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlKleurReflector import KlKleurReflector


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bebakening(Signalisatie, AIMObject):
    """Abstracte voor de bebakeningen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._kleurReflectorAflopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorAflopend',
                                                    label='kleur aflopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorAflopend',
                                                    definition='De kleur van de reflector stroomafwaarts.',
                                                    owner=self)

        self._kleurReflectorOplopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorOplopend',
                                                    label='kleur oplopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bebakening.kleurReflectorOplopend',
                                                    definition='De kleur van de reflector stroomopwaarts.',
                                                    owner=self)

    @property
    def kleurReflectorAflopend(self) -> str:
        """De kleur van de reflector stroomafwaarts."""
        return self._kleurReflectorAflopend.get_waarde()

    @kleurReflectorAflopend.setter
    def kleurReflectorAflopend(self, value):
        self._kleurReflectorAflopend.set_waarde(value, owner=self)

    @property
    def kleurReflectorOplopend(self) -> str:
        """De kleur van de reflector stroomopwaarts."""
        return self._kleurReflectorOplopend.get_waarde()

    @kleurReflectorOplopend.setter
    def kleurReflectorOplopend(self, value):
        self._kleurReflectorOplopend.set_waarde(value, owner=self)
