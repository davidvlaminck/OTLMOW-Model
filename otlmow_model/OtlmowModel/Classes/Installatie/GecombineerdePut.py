# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GecombineerdePut(AIMObject, PuntGeometrie):
    """Alle putrelaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GecombineerdePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
