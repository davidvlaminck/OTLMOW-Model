# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoogtebegrenzerInstallatie(AIMNaamObject, LijnGeometrie):
    """Een mechanische en/of elektronische opstelling die bij kunstwerken (zoals bruggen of tunnels) de maximale doorrijhoogte van voertuigen detecteert en overtredingen voorkomt om schade te vermijden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HoogtebegrenzerInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
