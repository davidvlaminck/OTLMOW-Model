# coding=utf-8
from typing import ClassVar

from ...BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNacht(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                          naam='retrotreflectiecoëfficiënt',
                                                          label='retrotreflectiecoëfficiënt',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht.retrotreflectiecoëfficiënt',
                                                          usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                          definition='De maat voor het retroreflecterend vermogen van een markering bij nacht.',
                                                          owner=self)

    @property
    def retrotreflectiecoëfficiënt(self) -> float:
        """De maat voor het retroreflecterend vermogen van een markering bij nacht."""
        return self._retrotreflectiecoëfficiënt.get_waarde()

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
