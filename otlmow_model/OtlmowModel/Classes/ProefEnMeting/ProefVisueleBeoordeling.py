# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVisueleBeoordeling(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Opsporen van de gebreken bij de definitieve oplevering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
