# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWateropslorping(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef waarbij de compactheid of poreusheid van het proefstuk door onderdompeling wordt bepaald."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

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
