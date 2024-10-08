# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcGeluidstestRapport import DtcGeluidstestRapport, DtcGeluidstestRapportWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefGeluidstest(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Test van het geluidsscherm op oa. luchtgeluidsisolatie, geluidsabsorptie, e.d."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._geluidstestrapport = OTLAttribuut(field=DtcGeluidstestRapport,
                                                naam='geluidstestrapport',
                                                label='geluidstestrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGeluidstest.geluidstestrapport',
                                                definition='Het resultaat geluidstest.',
                                                owner=self)

    @property
    def geluidstestrapport(self) -> DtcGeluidstestRapportWaarden:
        """Het resultaat geluidstest."""
        return self._geluidstestrapport.get_waarde()

    @geluidstestrapport.setter
    def geluidstestrapport(self, value):
        self._geluidstestrapport.set_waarde(value, owner=self)
