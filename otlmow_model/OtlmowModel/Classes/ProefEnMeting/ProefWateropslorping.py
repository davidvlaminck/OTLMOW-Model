# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWateropslorping(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef waarbij de compactheid of poreusheid van het proefstuk door onderdompeling wordt bepaald."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='o')  # o = direction: outgoing

        self._wateropslorping = OTLAttribuut(field=DtcDocument,
                                             naam='wateropslorping',
                                             label='wateropslorping',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping.wateropslorping',
                                             definition='Proef om de wateropslorping van de laag te bepalen.',
                                             owner=self)

    @property
    def wateropslorping(self) -> DtcDocumentWaarden:
        """Proef om de wateropslorping van de laag te bepalen."""
        return self._wateropslorping.get_waarde()

    @wateropslorping.setter
    def wateropslorping(self, value):
        self._wateropslorping.set_waarde(value, owner=self)
