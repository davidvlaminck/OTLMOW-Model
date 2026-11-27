# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefEffectiefBindmiddelgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid bitumen, uitgedrukt t.o.v. het totale mengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
