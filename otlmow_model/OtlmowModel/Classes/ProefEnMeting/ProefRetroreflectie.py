# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefRetroreflectie(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het bepalen van de retroreflectiecoëfficiënt via een manuele retroreflectometer of via labotesten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRetroreflectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', direction='o')  # o = direction: outgoing

        self._retroreflectie = OTLAttribuut(field=DtcDocument,
                                            naam='retroreflectie',
                                            label='retroreflectie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRetroreflectie.retroreflectie',
                                            definition='Proef om de retroreflectie van een verkeersbord te bepalen.',
                                            owner=self)

    @property
    def retroreflectie(self) -> DtcDocumentWaarden:
        """Proef om de retroreflectie van een verkeersbord te bepalen."""
        return self._retroreflectie.get_waarde()

    @retroreflectie.setter
    def retroreflectie(self, value):
        self._retroreflectie.set_waarde(value, owner=self)
