# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlVetType import KlVetType
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandheugel(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een recht of gekromd mechanisch element, ook wel tandlat of heugel genoemd, die aan één kant is voorzien van vertanding, zoals een tandwiel. De tanden grijpen in op die van een bijbehorend tandwiel, waardoor afhankelijk van de vorm zowel lineaire als roterende bewegingen kunnen worden gerealiseerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aangrijpingsstoel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagstoel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tandheugelmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._lengteTandheugel = OTLAttribuut(field=KwantWrdInMillimeter,
                                              naam='lengteTandheugel',
                                              label='lengte heugel',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel.lengteTandheugel',
                                              definition='De lengte van de tandheugel.',
                                              owner=self)

        self._typeVet = OTLAttribuut(field=KlVetType,
                                     naam='typeVet',
                                     label='type vet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandheugel.typeVet',
                                     definition='Geeft aan welk type vet gebruikt wordt om de tandheugel overbrenging te smeren.',
                                     owner=self)

    @property
    def lengteTandheugel(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de tandheugel."""
        return self._lengteTandheugel.get_waarde()

    @lengteTandheugel.setter
    def lengteTandheugel(self, value):
        self._lengteTandheugel.set_waarde(value, owner=self)

    @property
    def typeVet(self) -> str:
        """Geeft aan welk type vet gebruikt wordt om de tandheugel overbrenging te smeren."""
        return self._typeVet.get_waarde()

    @typeVet.setter
    def typeVet(self, value):
        self._typeVet.set_waarde(value, owner=self)
