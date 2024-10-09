# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefHechtsterkte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het resultaat van de trekproef waarbij een proefstuk wordt blootgesteld aan een stijgende spanning tot er een breuk optreedt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='o')  # o = direction: outgoing

        self._hechtsterkte = OTLAttribuut(field=DtcDocument,
                                          naam='hechtsterkte',
                                          label='hechtsterkte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte.hechtsterkte',
                                          definition='Proef om de hechtsterkte van de laag te bepalen.',
                                          owner=self)

    @property
    def hechtsterkte(self) -> DtcDocumentWaarden:
        """Proef om de hechtsterkte van de laag te bepalen."""
        return self._hechtsterkte.get_waarde()

    @hechtsterkte.setter
    def hechtsterkte(self, value):
        self._hechtsterkte.set_waarde(value, owner=self)
