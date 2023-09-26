# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Abstracten.ConstructieElement import ConstructieElement
from otlmow_model.Classes.Abstracten.ConstructieElementenGC import ConstructieElementenGC
from otlmow_model.Datatypes.DtcAfmetingBxlxhInM import DtcAfmetingBxlxhInM, DtcAfmetingBxlxhInMWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlPlaatsingswijzePlint import KlPlaatsingswijzePlint
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PlintGC(BetonnenConstructieElement, ConstructieElement, ConstructieElementenGC, LijnGeometrie):
    """Een plint is een betonnen balk/plaat die de akoestische dichtheid verzekert tussen de schermelementen van de geluidswerende constructie en de bodem."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram')

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInM,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.afmetingen',
                                        definition='Met dit complex datatype worden de afmetingen van de plint weergegeven. Indien de plint afwijkt van een rechthoekige vorm wordt deze informatie in de technische fiche opgeslagen.',
                                        owner=self)

        self._plaatsingswijze = OTLAttribuut(field=KlPlaatsingswijzePlint,
                                             naam='plaatsingswijze',
                                             label='plaatsingswijze',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.plaatsingswijze',
                                             definition='De manier waarop de plint geplaatst is ten opzichte van de profielen.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.technischeFiche',
                                             definition='Document met verdere specificaties van de plint die niet opgevangen worden met de aanwezige attributen.',
                                             owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInMWaarden:
        """Met dit complex datatype worden de afmetingen van de plint weergegeven. Indien de plint afwijkt van een rechthoekige vorm wordt deze informatie in de technische fiche opgeslagen."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def plaatsingswijze(self) -> str:
        """De manier waarop de plint geplaatst is ten opzichte van de profielen."""
        return self._plaatsingswijze.get_waarde()

    @plaatsingswijze.setter
    def plaatsingswijze(self, value):
        self._plaatsingswijze.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document met verdere specificaties van de plint die niet opgevangen worden met de aanwezige attributen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
