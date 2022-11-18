# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerankeringskracht(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Een trekproef in situ om de verankering van de ankerstaven in een betonverharding te testen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._verankeringskracht = OTLAttribuut(field=DtcDocument,
                                                naam='verankeringskracht',
                                                label='verankeringskracht',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht.verankeringskracht',
                                                definition='Het resultaat van de test om de verankeringskracht in de BV laag.',
                                                owner=self)

    @property
    def verankeringskracht(self) -> DtcDocumentWaarden:
        """Het resultaat van de test om de verankeringskracht in de BV laag."""
        return self._verankeringskracht.get_waarde()

    @verankeringskracht.setter
    def verankeringskracht(self, value):
        self._verankeringskracht.set_waarde(value, owner=self)
