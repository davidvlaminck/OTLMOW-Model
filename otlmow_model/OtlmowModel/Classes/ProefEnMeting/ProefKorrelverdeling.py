# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKorrelverdeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de doorval door een reeks zeven van een granulaatmengsel volgens NBN EN 933-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', direction='o')  # o = direction: outgoing

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
