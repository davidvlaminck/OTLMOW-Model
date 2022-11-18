# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtdichtheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Testen van de drukval van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put')

        self._luchtdichtheid = OTLAttribuut(field=DtcDocument,
                                            naam='luchtdichtheid',
                                            label='luchtdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid.luchtdichtheid',
                                            definition='Testresultaten van de opgemeten drukval van het beproefde leidingsvak.',
                                            owner=self)

    @property
    def luchtdichtheid(self) -> DtcDocumentWaarden:
        """Testresultaten van de opgemeten drukval van het beproefde leidingsvak."""
        return self._luchtdichtheid.get_waarde()

    @luchtdichtheid.setter
    def luchtdichtheid(self, value):
        self._luchtdichtheid.set_waarde(value, owner=self)
