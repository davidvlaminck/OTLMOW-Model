# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlOverigeFunctiesCentreerinrichting import (
    KlOverigeFunctiesCentreerinrichting,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Centreerinrichting(AIMNaamObject, PuntGeometrie):
    """Een centreerinrichting is een constructieonderdeel dat een beweegbaar constructieonderdeel begeleidt opdat het zich correct positioneert tijdens het uitvoeren van een beweging. Meestal wordt die aangesproken nét alvorens het rust op de vaste steunpunten. Zowel de vaste constructie als de bewegende constructie kunnen er van voorzien zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreerinrichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._overigeFuncties = OTLAttribuut(field=KlOverigeFunctiesCentreerinrichting,
                                             naam='overigeFuncties',
                                             label='overige functies',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreerinrichting.overigeFuncties',
                                             definition='De overige functies van de centreerinrichting.',
                                             owner=self)

    @property
    def overigeFuncties(self) -> str:
        """De overige functies van de centreerinrichting."""
        return self._overigeFuncties.get_waarde()

    @overigeFuncties.setter
    def overigeFuncties(self, value):
        self._overigeFuncties.set_waarde(value, owner=self)
