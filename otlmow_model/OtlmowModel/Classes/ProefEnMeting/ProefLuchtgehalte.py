# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef die de hoeveelheid lucht bepaalt in vers beton met de drukmethode volgens NBN EN 12350-7."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='o')  # o = direction: outgoing

        self._luchtgehalte = OTLAttribuut(field=DtcDocument,
                                          naam='luchtgehalte',
                                          label='luchtgehalte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte.luchtgehalte',
                                          definition='Proefresultaten van het luchtgehalte.',
                                          owner=self)

    @property
    def luchtgehalte(self) -> DtcDocumentWaarden:
        """Proefresultaten van het luchtgehalte."""
        return self._luchtgehalte.get_waarde()

    @luchtgehalte.setter
    def luchtgehalte(self, value):
        self._luchtgehalte.set_waarde(value, owner=self)
