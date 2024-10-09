# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDraineervermogen(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de waterdoorlatendheid van een open verharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='o')  # o = direction: outgoing

        self._draineervermogen = OTLAttribuut(field=DtcDocument,
                                              naam='draineervermogen',
                                              label='draineervermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen.draineervermogen',
                                              definition='Proefresultaten van het drainvermogen.',
                                              owner=self)

    @property
    def draineervermogen(self) -> DtcDocumentWaarden:
        """Proefresultaten van het drainvermogen."""
        return self._draineervermogen.get_waarde()

    @draineervermogen.setter
    def draineervermogen(self, value):
        self._draineervermogen.set_waarde(value, owner=self)
