# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BekledingComponent import BekledingComponent
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBevestigingsMateriaalBrandwerendeBekleding import KlBevestigingsMateriaalBrandwerendeBekleding
from ...Datatypes.KlBrandkromme import KlBrandkromme
from ...Datatypes.KlTestnorm import KlTestnorm
from ...Datatypes.KlTypeBrandwerendeBekleding import KlTypeBrandwerendeBekleding
from ...Datatypes.KwantWrdInCelsius import KwantWrdInCelsius, KwantWrdInCelsiusWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BrandwerendeBekleding(BekledingComponent):
    """Bekleding die op de wanden of andere oppervlakken van een constructie wordt aangebracht met als functie de achterliggende constructie gedurende een bepaalde tijd te beschermen tegen de effecten van brand, door warmteoverdracht te beperken en structurele integriteit te behouden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding'
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

        self._bevestigingsmateriaal = OTLAttribuut(field=KlBevestigingsMateriaalBrandwerendeBekleding,
                                                   naam='bevestigingsmateriaal',
                                                   label='bevestigingsmateriaal',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.bevestigingsmateriaal',
                                                   definition='Het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd.',
                                                   owner=self)

        self._brandkromme = OTLAttribuut(field=KlBrandkromme,
                                         naam='brandkromme',
                                         label='brandkromme',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.brandkromme',
                                         definition='De specifieke temperatuur-tijdscurve (bv. RWS, ISO-834, HC) die als belasting is gehanteerd bij de validatie van de brandweerstand.',
                                         owner=self)

        self._brandweerstand = OTLAttribuut(field=KwantWrdInMinuut,
                                            naam='brandweerstand',
                                            label='brandweerstand',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.brandweerstand',
                                            definition='Geeft aan hoeveel minuten de bekleding bestand is tegen brand.',
                                            owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.dikte',
                                   definition='De nominale dikte van de aangebrachte beschermlaag, uitgedrukt in millimeter.',
                                   owner=self)

        self._maximaleTemperatuurinterface = OTLAttribuut(field=KwantWrdInCelsius,
                                                          naam='maximaleTemperatuurinterface',
                                                          label='maximale temperatuurinterface',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.maximaleTemperatuurinterface',
                                                          definition='De maximale temperatuur tegen dewelke de interface bestand is, uitgedrukt in graden celsius.',
                                                          owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.technischeFiche',
                                             definition='Het document met de productspecificaties, verwerkingsvoorschriften en prestatie-eigenschappen.',
                                             owner=self)

        self._testnorm = OTLAttribuut(field=KlTestnorm,
                                      naam='testnorm',
                                      label='testnorm',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.testnorm',
                                      definition='De norm of standaard (bv. NBN EN 13501) volgens dewelke de brandwerende eigenschappen van het materiaal zijn getest en gecertificeerd.',
                                      owner=self)

        self._type = OTLAttribuut(field=KlTypeBrandwerendeBekleding,
                                  naam='type',
                                  label='type brandwerende bekleding',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding.type',
                                  definition='De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescerende coating.',
                                  owner=self)

    @property
    def bevestigingsmateriaal(self) -> str:
        """Het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd."""
        return self._bevestigingsmateriaal.get_waarde()

    @bevestigingsmateriaal.setter
    def bevestigingsmateriaal(self, value):
        self._bevestigingsmateriaal.set_waarde(value, owner=self)

    @property
    def brandkromme(self) -> str:
        """De specifieke temperatuur-tijdscurve (bv. RWS, ISO-834, HC) die als belasting is gehanteerd bij de validatie van de brandweerstand."""
        return self._brandkromme.get_waarde()

    @brandkromme.setter
    def brandkromme(self, value):
        self._brandkromme.set_waarde(value, owner=self)

    @property
    def brandweerstand(self) -> KwantWrdInMinuutWaarden:
        """Geeft aan hoeveel minuten de bekleding bestand is tegen brand."""
        return self._brandweerstand.get_waarde()

    @brandweerstand.setter
    def brandweerstand(self, value):
        self._brandweerstand.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De nominale dikte van de aangebrachte beschermlaag, uitgedrukt in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def maximaleTemperatuurinterface(self) -> KwantWrdInCelsiusWaarden:
        """De maximale temperatuur tegen dewelke de interface bestand is, uitgedrukt in graden celsius."""
        return self._maximaleTemperatuurinterface.get_waarde()

    @maximaleTemperatuurinterface.setter
    def maximaleTemperatuurinterface(self, value):
        self._maximaleTemperatuurinterface.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Het document met de productspecificaties, verwerkingsvoorschriften en prestatie-eigenschappen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def testnorm(self) -> str:
        """De norm of standaard (bv. NBN EN 13501) volgens dewelke de brandwerende eigenschappen van het materiaal zijn getest en gecertificeerd."""
        return self._testnorm.get_waarde()

    @testnorm.setter
    def testnorm(self, value):
        self._testnorm.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescerende coating."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
