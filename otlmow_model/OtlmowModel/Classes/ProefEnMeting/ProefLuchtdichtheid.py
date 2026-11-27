# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuchtdichtheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Testen van de drukval van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
