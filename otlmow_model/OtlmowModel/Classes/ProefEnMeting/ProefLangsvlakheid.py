# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLangsvlakheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De controle van de langsvlakheid nieuwe verhardingen bij verschillende golflengten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._langsvlakheid = OTLAttribuut(field=DtcDocument,
                                           naam='langsvlakheid',
                                           label='langsvlakheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid.langsvlakheid',
                                           definition='Het resultaat van de meting.',
                                           owner=self)

    @property
    def langsvlakheid(self) -> DtcDocumentWaarden:
        """Het resultaat van de meting."""
        return self._langsvlakheid.get_waarde()

    @langsvlakheid.setter
    def langsvlakheid(self, value):
        self._langsvlakheid.set_waarde(value, owner=self)
