# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKorrelverdeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de doorval door een reeks zeven van een granulaatmengsel volgens NBN EN 933-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging')

        self._korrelverdeling = OTLAttribuut(field=DtcDocument,
                                             naam='korrelverdeling',
                                             label='korrelverdeling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling.korrelverdeling',
                                             definition='Het resultaat van de test van de gemeten korrelverdeling in de BV laag.',
                                             owner=self)

    @property
    def korrelverdeling(self) -> DtcDocumentWaarden:
        """Het resultaat van de test van de gemeten korrelverdeling in de BV laag."""
        return self._korrelverdeling.get_waarde()

    @korrelverdeling.setter
    def korrelverdeling(self, value):
        self._korrelverdeling.set_waarde(value, owner=self)
