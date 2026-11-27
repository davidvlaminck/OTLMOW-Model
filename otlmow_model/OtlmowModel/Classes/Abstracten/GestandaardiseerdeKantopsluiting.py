# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kantopsluiting import Kantopsluiting
from ...Datatypes.KlLEKantopsluitingBijkomendeParameter import (
    KlLEKantopsluitingBijkomendeParameter,
)
from ...Datatypes.KlLEStandaardFabricageLengte import KlLEStandaardFabricageLengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class GestandaardiseerdeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die voldoet aan een bepaalde standaard."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bijkomendeParameter = OTLAttribuut(field=KlLEKantopsluitingBijkomendeParameter,
                                                 naam='bijkomendeParameter',
                                                 label='bijkomende parameter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.bijkomendeParameter',
                                                 definition='Detail typering van de kantopsluiting.',
                                                 owner=self)

        self._fabricageLengte = OTLAttribuut(field=KlLEStandaardFabricageLengte,
                                             naam='fabricageLengte',
                                             label='fabricagelengte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.fabricageLengte',
                                             definition='De lengte van de individuele kantopsluiting volgens de norm.',
                                             owner=self)

    @property
    def bijkomendeParameter(self) -> str:
        """Detail typering van de kantopsluiting."""
        return self._bijkomendeParameter.get_waarde()

    @bijkomendeParameter.setter
    def bijkomendeParameter(self, value):
        self._bijkomendeParameter.set_waarde(value, owner=self)

    @property
    def fabricageLengte(self) -> str:
        """De lengte van de individuele kantopsluiting volgens de norm."""
        return self._fabricageLengte.get_waarde()

    @fabricageLengte.setter
    def fabricageLengte(self, value):
        self._fabricageLengte.set_waarde(value, owner=self)
