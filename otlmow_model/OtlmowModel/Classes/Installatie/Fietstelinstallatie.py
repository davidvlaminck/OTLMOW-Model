# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fietstelinstallatie(NaampadObject, PuntGeometrie, VlakGeometrie):
    """Groepering van onderdelen die samen een installatie vormen voor het verzamelen van telgegevens over passerende fietsers en in sommige installaties het tonenvan de gegevens."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fietstelinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
