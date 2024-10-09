# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefBindmiddeldosering(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de hoeveelheid bindmiddel te bepalen die nodig is om de grond als funderingslaag te garanderen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw', direction='o')  # o = direction: outgoing

        self._technischVerslagBindmiddeldosering = OTLAttribuut(field=DtcDocument,
                                                                naam='technischVerslagBindmiddeldosering',
                                                                label='technisch verslag bindmiddeldosering',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering.technischVerslagBindmiddeldosering',
                                                                definition='Het technisch verslag van een aangewezen bindmiddeldosering.',
                                                                owner=self)

    @property
    def technischVerslagBindmiddeldosering(self) -> DtcDocumentWaarden:
        """Het technisch verslag van een aangewezen bindmiddeldosering."""
        return self._technischVerslagBindmiddeldosering.get_waarde()

    @technischVerslagBindmiddeldosering.setter
    def technischVerslagBindmiddeldosering(self, value):
        self._technischVerslagBindmiddeldosering.set_waarde(value, owner=self)
