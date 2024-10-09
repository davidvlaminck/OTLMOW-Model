# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BekledingComponent import BekledingComponent
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcVoorzetconstructieBevestigingsmateriaal import DtcVoorzetconstructieBevestigingsmateriaal, DtcVoorzetconstructieBevestigingsmateriaalWaarden
from ...Datatypes.KwantWrdInCelsius import KwantWrdInCelsius, KwantWrdInCelsiusWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voorzetconstructie(BekledingComponent):
    """Een voorzetconstructie is een wandconstructie die vóór een bestaande muur wordt geplaatst. Doorgaans uitgevoerd met kleine spouw met isolatiemateriaal en aan de binnenzijde van het bouw- of kunstwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional

        self._bevestigingsmateriaal = OTLAttribuut(field=DtcVoorzetconstructieBevestigingsmateriaal,
                                                   naam='bevestigingsmateriaal',
                                                   label='bevestigingsmateriaal',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.bevestigingsmateriaal',
                                                   definition='Het materiaal met dewelke de voorzetconstructie bevestigd is aan bijvoorbeeld een wand.',
                                                   owner=self)

        self._brandweerstand = OTLAttribuut(field=KwantWrdInMinuut,
                                            naam='brandweerstand',
                                            label='brandweerstand',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.brandweerstand',
                                            definition='Geeft aan hoeveel minuten de voorzetconstructie bestand is tegen brand.',
                                            owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.dikte',
                                   definition='De dikte van de voorzetconstructie, uitgedrukt in millimeter.',
                                   owner=self)

        self._getestOpSpalling = OTLAttribuut(field=BooleanField,
                                              naam='getestOpSpalling',
                                              label='getest op spalling',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.getestOpSpalling',
                                              definition='Geeft aan of de voorzetconstructie al dan niet getest is op spalling.',
                                              owner=self)

        self._isBrandwerend = OTLAttribuut(field=BooleanField,
                                           naam='isBrandwerend',
                                           label='is brandwerend',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.isBrandwerend',
                                           definition='Geeft aan of de voorzetconstructie al dan niet brandwerend is.',
                                           owner=self)

        self._maximaleInterfaceTemperatuur = OTLAttribuut(field=KwantWrdInCelsius,
                                                          naam='maximaleInterfaceTemperatuur',
                                                          label='maximale temperatuur interface',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.maximaleInterfaceTemperatuur',
                                                          definition='De maximale temperatuur tegen dewelke de interface bestand is, uitgedrukt in graden celsius.',
                                                          owner=self)

        self._technischefiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischefiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie.technischefiche',
                                             definition='De technische fiche, al dan niet met het certificaat, van de voorzetconstructie.',
                                             owner=self)

    @property
    def bevestigingsmateriaal(self) -> DtcVoorzetconstructieBevestigingsmateriaalWaarden:
        """Het materiaal met dewelke de voorzetconstructie bevestigd is aan bijvoorbeeld een wand."""
        return self._bevestigingsmateriaal.get_waarde()

    @bevestigingsmateriaal.setter
    def bevestigingsmateriaal(self, value):
        self._bevestigingsmateriaal.set_waarde(value, owner=self)

    @property
    def brandweerstand(self) -> KwantWrdInMinuutWaarden:
        """Geeft aan hoeveel minuten de voorzetconstructie bestand is tegen brand."""
        return self._brandweerstand.get_waarde()

    @brandweerstand.setter
    def brandweerstand(self, value):
        self._brandweerstand.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de voorzetconstructie, uitgedrukt in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def getestOpSpalling(self) -> bool:
        """Geeft aan of de voorzetconstructie al dan niet getest is op spalling."""
        return self._getestOpSpalling.get_waarde()

    @getestOpSpalling.setter
    def getestOpSpalling(self, value):
        self._getestOpSpalling.set_waarde(value, owner=self)

    @property
    def isBrandwerend(self) -> bool:
        """Geeft aan of de voorzetconstructie al dan niet brandwerend is."""
        return self._isBrandwerend.get_waarde()

    @isBrandwerend.setter
    def isBrandwerend(self, value):
        self._isBrandwerend.set_waarde(value, owner=self)

    @property
    def maximaleInterfaceTemperatuur(self) -> KwantWrdInCelsiusWaarden:
        """De maximale temperatuur tegen dewelke de interface bestand is, uitgedrukt in graden celsius."""
        return self._maximaleInterfaceTemperatuur.get_waarde()

    @maximaleInterfaceTemperatuur.setter
    def maximaleInterfaceTemperatuur(self, value):
        self._maximaleInterfaceTemperatuur.set_waarde(value, owner=self)

    @property
    def technischefiche(self) -> DtcDocumentWaarden:
        """De technische fiche, al dan niet met het certificaat, van de voorzetconstructie."""
        return self._technischefiche.get_waarde()

    @technischefiche.setter
    def technischefiche(self, value):
        self._technischefiche.set_waarde(value, owner=self)
