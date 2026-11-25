# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kokerruimte import Kokerruimte
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class DrogePompkelder(Kokerruimte, AIMNaamObject):
    """Een droge pompkelder is dat gedeelte van een gebouw/kunstwerk dat (meestal) onder het maaiveld is gelegen,veelal om beheersvoorzieningen te herbergen en/of als een technische ruimte dat deel uitmaakt van een pompstation."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HijsEnHefwerktuig', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie', 'u', '2.21.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isOndergronds = OTLAttribuut(field=BooleanField,
                                           naam='isOndergronds',
                                           label='is ondergronds',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder.isOndergronds',
                                           definition='Geeft aan of de droge pompkelder zich boven- of ondergronds bevindt.',
                                           owner=self)

    @property
    def isOndergronds(self) -> bool:
        """Geeft aan of de droge pompkelder zich boven- of ondergronds bevindt."""
        return self._isOndergronds.get_waarde()

    @isOndergronds.setter
    def isOndergronds(self, value):
        self._isOndergronds.set_waarde(value, owner=self)
