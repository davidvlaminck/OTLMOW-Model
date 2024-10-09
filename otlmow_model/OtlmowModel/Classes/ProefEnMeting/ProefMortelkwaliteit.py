# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefMortelkwaliteit(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de sterkte van voegmortel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw', direction='o')  # o = direction: outgoing

        self._mortelkwaliteit = OTLAttribuut(field=DtcDocument,
                                             naam='mortelkwaliteit',
                                             label='mortelkwaliteit',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit.mortelkwaliteit',
                                             definition='Een rapport van de mortelkwaliteit van de onderbouw laag.',
                                             owner=self)

    @property
    def mortelkwaliteit(self) -> DtcDocumentWaarden:
        """Een rapport van de mortelkwaliteit van de onderbouw laag."""
        return self._mortelkwaliteit.get_waarde()

    @mortelkwaliteit.setter
    def mortelkwaliteit(self, value):
        self._mortelkwaliteit.set_waarde(value, owner=self)
