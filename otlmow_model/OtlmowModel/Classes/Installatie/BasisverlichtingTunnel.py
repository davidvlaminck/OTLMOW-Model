# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BasisverlichtingTunnel(AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Het geheel van verlichtingstoestellen dat over de hele lengte van de koker loopt en met verschillende regimes het verlichtingsniveau voor de koker kan bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BasisverlichtingTunnel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tunnelverlichting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LSSchuif', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
