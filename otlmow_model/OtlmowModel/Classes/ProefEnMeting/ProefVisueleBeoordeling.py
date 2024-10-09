# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVisueleBeoordeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Opsporen van de gebreken bij de definitieve oplevering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag', direction='o')  # o = direction: outgoing

        self._visueleBeoordeling = OTLAttribuut(field=DtcDocument,
                                                naam='visueleBeoordeling',
                                                label='visuele beoordeling',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling.visueleBeoordeling',
                                                definition='Een rapport van de visuele beoordeling van de laag.',
                                                owner=self)

    @property
    def visueleBeoordeling(self) -> DtcDocumentWaarden:
        """Een rapport van de visuele beoordeling van de laag."""
        return self._visueleBeoordeling.get_waarde()

    @visueleBeoordeling.setter
    def visueleBeoordeling(self, value):
        self._visueleBeoordeling.set_waarde(value, owner=self)
