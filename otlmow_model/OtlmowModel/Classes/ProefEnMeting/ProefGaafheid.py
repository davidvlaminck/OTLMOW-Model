# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGaafheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van het lijnvormig element op de ongeschondenheid, volledigheid en zuiverheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='o')  # o = direction: outgoing

        self._gaafheid = OTLAttribuut(field=DtcDocument,
                                      naam='gaafheid',
                                      label='gaafheid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid.gaafheid',
                                      definition='De resultaten van de controle.',
                                      owner=self)

    @property
    def gaafheid(self) -> DtcDocumentWaarden:
        """De resultaten van de controle."""
        return self._gaafheid.get_waarde()

    @gaafheid.setter
    def gaafheid(self, value):
        self._gaafheid.set_waarde(value, owner=self)
