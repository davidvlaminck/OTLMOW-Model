# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefConsistentie(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Zetmaat van betonspecie volgens NBN EN 12350-2 bij een cementbetonverharding of een lijnvormig element."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._consistentie = OTLAttribuut(field=DtcDocument,
                                          naam='consistentie',
                                          label='consistentie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie.consistentie',
                                          definition='Proefresultaten van de consistentie.',
                                          owner=self)

    @property
    def consistentie(self) -> DtcDocumentWaarden:
        """Proefresultaten van de consistentie."""
        return self._consistentie.get_waarde()

    @consistentie.setter
    def consistentie(self, value):
        self._consistentie.set_waarde(value, owner=self)
