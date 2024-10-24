# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGrondkarakteristieken(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de grondeigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', direction='o')  # o = direction: outgoing

        self._bepalingGrondkarakteristieken = OTLAttribuut(field=DtcDocument,
                                                           naam='bepalingGrondkarakteristieken',
                                                           label='bepaling grondkarakteristieken',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGrondkarakteristieken.bepalingGrondkarakteristieken',
                                                           definition='Proef met de resultaten van de grondkarakteristieken.',
                                                           owner=self)

    @property
    def bepalingGrondkarakteristieken(self) -> DtcDocumentWaarden:
        """Proef met de resultaten van de grondkarakteristieken."""
        return self._bepalingGrondkarakteristieken.get_waarde()

    @bepalingGrondkarakteristieken.setter
    def bepalingGrondkarakteristieken(self, value):
        self._bepalingGrondkarakteristieken.set_waarde(value, owner=self)
