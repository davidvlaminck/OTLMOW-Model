# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecotunnel(AIMObject, VlakGeometrie):
    """Een (grote) ecotunnel is een tunnel onder een grote weg, waarlangs dieren veilig de overkant kunnen bereiken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecotunnel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleiding', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
