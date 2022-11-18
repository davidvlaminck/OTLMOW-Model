# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefMortelkwaliteit(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de sterkte van voegmortel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefMortelkwaliteit'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw')

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
