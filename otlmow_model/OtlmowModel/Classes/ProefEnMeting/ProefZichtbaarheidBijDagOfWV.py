# coding=utf-8
from typing import ClassVar

from ...BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijDagOfWV(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de luminantiecoëfficiënt bij diffuse verlichting van een gemarkeerd oppervlak (Qd) bij daglicht of onder openbare verlichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._luminantiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                     naam='luminantiecoëfficiënt',
                                                     label='luminantiecoëfficient',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV.luminantiecoëfficiënt',
                                                     usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                     definition='De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak.',
                                                     owner=self)

    @property
    def luminantiecoëfficiënt(self) -> float:
        """De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak."""
        return self._luminantiecoëfficiënt.get_waarde()

    @luminantiecoëfficiënt.setter
    def luminantiecoëfficiënt(self, value):
        self._luminantiecoëfficiënt.set_waarde(value, owner=self)
