# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerderOnderzoekTrekproef(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Een trekproef is een manier om nader te onderzoeken hoe het met de veiligheid van een (aangetaste of beschadigde) boom gesteld is. Door met een lier effectief aan een boom te trekken wordt de belasting bij storm in een model gegoten en getest."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom', 'o', '2.0.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._verderOnderzoekTrekproef = OTLAttribuut(field=DtcDocument,
                                                      naam='verderOnderzoekTrekproef',
                                                      label='verder onderzoek trekproef',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef.verderOnderzoekTrekproef',
                                                      kardinaliteit_max='*',
                                                      definition='Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) van bomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van de stamvoet.',
                                                      owner=self)

    @property
    def verderOnderzoekTrekproef(self) -> list[DtcDocumentWaarden]:
        """Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) van bomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van de stamvoet."""
        return self._verderOnderzoekTrekproef.get_waarde()

    @verderOnderzoekTrekproef.setter
    def verderOnderzoekTrekproef(self, value):
        self._verderOnderzoekTrekproef.set_waarde(value, owner=self)
