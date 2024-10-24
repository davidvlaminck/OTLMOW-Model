# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWaterdichtheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Testen van het waterverlies van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put', direction='o')  # o = direction: outgoing

        self._waterdichtheid = OTLAttribuut(field=DtcDocument,
                                            naam='waterdichtheid',
                                            label='waterdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid.waterdichtheid',
                                            definition='Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak.',
                                            owner=self)

    @property
    def waterdichtheid(self) -> DtcDocumentWaarden:
        """Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak."""
        return self._waterdichtheid.get_waarde()

    @waterdichtheid.setter
    def waterdichtheid(self, value):
        self._waterdichtheid.set_waarde(value, owner=self)
