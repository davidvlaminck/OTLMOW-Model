# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cilinderzuiger(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Het onderdeel dat de cilinder in twee kamers verdeelt, waardoor het hydraulische drukverschil de cilinderstang doet bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderzuiger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dichting', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
