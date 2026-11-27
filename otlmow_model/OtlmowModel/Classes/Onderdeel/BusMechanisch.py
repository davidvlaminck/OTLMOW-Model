# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalBusEnRing import KlMateriaalBusEnRing
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BusMechanisch(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een cilindervormig onderdeel dat vaak als voering of geleider wordt gebruikt in mechanische verbindingen. Voorbeelden hiervan zijn afstandsbus en demontagebus. De hoogte is groter dan de wanddikte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BusMechanisch'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Scharnierpunt', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._materiaalBus = OTLAttribuut(field=KlMateriaalBusEnRing,
                                          naam='materiaalBus',
                                          label='materiaal bus',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BusMechanisch.materiaalBus',
                                          definition='Het materiaal waaruit de bus is vervaardigd.',
                                          owner=self)

    @property
    def materiaalBus(self) -> str:
        """Het materiaal waaruit de bus is vervaardigd."""
        return self._materiaalBus.get_waarde()

    @materiaalBus.setter
    def materiaalBus(self, value):
        self._materiaalBus.set_waarde(value, owner=self)
