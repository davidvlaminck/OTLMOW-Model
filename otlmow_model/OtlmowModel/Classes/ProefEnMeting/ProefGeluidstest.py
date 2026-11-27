# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcGeluidstestRapport import (
    DtcGeluidstestRapport,
    DtcGeluidstestRapportWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', 'o', '2.0.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._geluidstestrapport = OTLAttribuut(field=DtcGeluidstestRapport,
                                                naam='geluidstestrapport',
                                                label='geluidstestrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest.geluidstestrapport',
                                                definition='Het resultaat geluidstest.',
                                                owner=self)

    @property
    def geluidstestrapport(self) -> DtcGeluidstestRapportWaarden:
        """Het resultaat geluidstest."""
        return self._geluidstestrapport.get_waarde()

    @geluidstestrapport.setter
    def geluidstestrapport(self, value):
        self._geluidstestrapport.set_waarde(value, owner=self)
