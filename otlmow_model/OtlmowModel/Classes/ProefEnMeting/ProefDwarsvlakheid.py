# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDwarsvlakheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de spoorvorming via de latmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='o')  # o = direction: outgoing

        self._dwarsvlakheid = OTLAttribuut(field=DtcDocument,
                                           naam='dwarsvlakheid',
                                           label='dwarsvlakheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid.dwarsvlakheid',
                                           definition='Proefresultaten van de dwarsvlakheid.',
                                           owner=self)

    @property
    def dwarsvlakheid(self) -> DtcDocumentWaarden:
        """Proefresultaten van de dwarsvlakheid."""
        return self._dwarsvlakheid.get_waarde()

    @dwarsvlakheid.setter
    def dwarsvlakheid(self, value):
        self._dwarsvlakheid.set_waarde(value, owner=self)
