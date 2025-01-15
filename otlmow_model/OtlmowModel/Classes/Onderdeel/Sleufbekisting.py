# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlUitvoeringsmethodeBekisting import KlUitvoeringsmethodeBekisting
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sleufbekisting(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een kistsysteem (synoniemen: boxen, Verbau-systeem of grootvlakbeschoeiing) om sleuven/bouwputten te beschoeien. De kist kan op verschillende manieren opgebouwd worden. Enkel grondkerend en bedoeld als tijdelijke beschoeiing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleufbekisting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional

        self._beschoeiingslengte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='beschoeiingslengte',
                                                label='beschoeiingslengte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleufbekisting.beschoeiingslengte',
                                                definition='Lengte van beschoeiing in meter.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleufbekisting.technischeFiche',
                                             definition='Technische fiche met technische details van de uitvoering van de sleufbekisting.',
                                             owner=self)

        self._uitvoeringsmethode = OTLAttribuut(field=KlUitvoeringsmethodeBekisting,
                                                naam='uitvoeringsmethode',
                                                label='uitvoeringsmethode',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleufbekisting.uitvoeringsmethode',
                                                definition='De verschillende uitvoeringsmogelijkheden.',
                                                owner=self)

    @property
    def beschoeiingslengte(self) -> KwantWrdInMeterWaarden:
        """Lengte van beschoeiing in meter."""
        return self._beschoeiingslengte.get_waarde()

    @beschoeiingslengte.setter
    def beschoeiingslengte(self, value):
        self._beschoeiingslengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche met technische details van de uitvoering van de sleufbekisting."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethode(self) -> str:
        """De verschillende uitvoeringsmogelijkheden."""
        return self._uitvoeringsmethode.get_waarde()

    @uitvoeringsmethode.setter
    def uitvoeringsmethode(self, value):
        self._uitvoeringsmethode.set_waarde(value, owner=self)
