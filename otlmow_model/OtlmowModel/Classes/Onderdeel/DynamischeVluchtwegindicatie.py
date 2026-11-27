# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynamischeVluchtwegindicatie(AIMObject, PuntGeometrie):
    """Armaturen die ingezet worden indien er alternatieve vluchtconcepten worden toegepast. De vluchtroute loopt dan meestal gedeeltelijk door de ondersteunende koker. De borden geven de te volgen vluchtroute aan en zijn pas zichtbaar zodra ze worden ingeschakeld. Bij evacuatie kan er ook een extra ondersteunende omroepbericht worden ingezet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynamischeVluchtwegindicatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
