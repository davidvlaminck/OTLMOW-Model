# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefEffectiefBindmiddelgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid bitumen, uitgedrukt t.o.v. het totale mengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', direction='o')  # o = direction: outgoing

        self._effectiefBindmiddelgehalte = OTLAttribuut(field=DtcDocument,
                                                        naam='effectiefBindmiddelgehalte',
                                                        label='effectief bindmiddelgehalte',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte.effectiefBindmiddelgehalte',
                                                        definition='Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag.',
                                                        owner=self)

    @property
    def effectiefBindmiddelgehalte(self) -> DtcDocumentWaarden:
        """Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag."""
        return self._effectiefBindmiddelgehalte.get_waarde()

    @effectiefBindmiddelgehalte.setter
    def effectiefBindmiddelgehalte(self, value):
        self._effectiefBindmiddelgehalte.set_waarde(value, owner=self)
