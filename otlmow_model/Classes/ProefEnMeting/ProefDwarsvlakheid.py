# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDwarsvlakheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de spoorvorming via de latmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')

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
