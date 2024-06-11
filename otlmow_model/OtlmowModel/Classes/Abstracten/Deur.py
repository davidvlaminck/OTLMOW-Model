# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Toegangselement import Toegangselement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM, DtcAfmetingBxhInMWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlDeurFabrikant import KlDeurFabrikant
from ...Datatypes.KlDeurHandgreeptype import KlDeurHandgreeptype
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInSeconde import KwantWrdInSeconde, KwantWrdInSecondeWaarden
from ...Datatypes.KwantWrdInUur import KwantWrdInUur, KwantWrdInUurWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deur(Toegangselement):
    """Een beweegbaar element ter afsluiting van een ruimte. In een gebouw is een deur meestal bevestigd in een kozijn,dat weer in een muur of wand is aangebracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.9.0'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._afmetingDeuropening = OTLAttribuut(field=DtcAfmetingBxhInM,
                                                 naam='afmetingDeuropening',
                                                 label='afmeting deuropening',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.afmetingDeuropening',
                                                 usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                                 deprecated_version='2.9.0',
                                                 definition='Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is.',
                                                 owner=self)

        self._brandweerstand = OTLAttribuut(field=KwantWrdInUur,
                                            naam='brandweerstand',
                                            label='brandweerstand',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.brandweerstand',
                                            usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                            deprecated_version='2.9.0',
                                            definition='Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand.',
                                            owner=self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.breedte',
                                     usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                     deprecated_version='2.9.0',
                                     definition='De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.dikte',
                                   usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                   deprecated_version='2.9.0',
                                   definition='De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere.',
                                   owner=self)

        self._fabrikant = OTLAttribuut(field=KlDeurFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.fabrikant',
                                       usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                       deprecated_version='2.9.0',
                                       definition='Naam van de producent van de deur.',
                                       owner=self)

        self._handgreeptype = OTLAttribuut(field=KlDeurHandgreeptype,
                                           naam='handgreeptype',
                                           label='handgreeptype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.handgreeptype',
                                           usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                           deprecated_version='2.9.0',
                                           definition='Soort greep aan waarmee de deur geopend wordt.',
                                           owner=self)

        self._heeftDeurcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftDeurcontact',
                                              label='heeft deurcontact',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.heeftDeurcontact',
                                              usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                              deprecated_version='2.9.0',
                                              definition='Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is.',
                                              owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.hoogte',
                                    usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                    deprecated_version='2.9.0',
                                    definition='De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant.',
                                    owner=self)

        self._isZelfsluitend = OTLAttribuut(field=BooleanField,
                                            naam='isZelfsluitend',
                                            label='is zelfsluitend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.isZelfsluitend',
                                            usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                            deprecated_version='2.9.0',
                                            definition='Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker.',
                                            owner=self)

        self._ophangconstructie = OTLAttribuut(field=DtcDocument,
                                               naam='ophangconstructie',
                                               label='ophangconstructie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.ophangconstructie',
                                               usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                               deprecated_version='2.9.0',
                                               definition='Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt.',
                                               owner=self)

        self._sluitingstijd = OTLAttribuut(field=KwantWrdInSeconde,
                                           naam='sluitingstijd',
                                           label='sluitingstijd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.sluitingstijd',
                                           usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                           deprecated_version='2.9.0',
                                           definition='Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat.',
                                           owner=self)

    @property
    def afmetingDeuropening(self) -> DtcAfmetingBxhInMWaarden:
        """Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is."""
        return self._afmetingDeuropening.get_waarde()

    @afmetingDeuropening.setter
    def afmetingDeuropening(self, value):
        self._afmetingDeuropening.set_waarde(value, owner=self)

    @property
    def brandweerstand(self) -> KwantWrdInUurWaarden:
        """Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand."""
        return self._brandweerstand.get_waarde()

    @brandweerstand.setter
    def brandweerstand(self, value):
        self._brandweerstand.set_waarde(value, owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def fabrikant(self) -> str:
        """Naam van de producent van de deur."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def handgreeptype(self) -> str:
        """Soort greep aan waarmee de deur geopend wordt."""
        return self._handgreeptype.get_waarde()

    @handgreeptype.setter
    def handgreeptype(self, value):
        self._handgreeptype.set_waarde(value, owner=self)

    @property
    def heeftDeurcontact(self) -> bool:
        """Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is."""
        return self._heeftDeurcontact.get_waarde()

    @heeftDeurcontact.setter
    def heeftDeurcontact(self, value):
        self._heeftDeurcontact.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isZelfsluitend(self) -> bool:
        """Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker."""
        return self._isZelfsluitend.get_waarde()

    @isZelfsluitend.setter
    def isZelfsluitend(self, value):
        self._isZelfsluitend.set_waarde(value, owner=self)

    @property
    def ophangconstructie(self) -> DtcDocumentWaarden:
        """Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt."""
        return self._ophangconstructie.get_waarde()

    @ophangconstructie.setter
    def ophangconstructie(self, value):
        self._ophangconstructie.set_waarde(value, owner=self)

    @property
    def sluitingstijd(self) -> KwantWrdInSecondeWaarden:
        """Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat."""
        return self._sluitingstijd.get_waarde()

    @sluitingstijd.setter
    def sluitingstijd(self, value):
        self._sluitingstijd.set_waarde(value, owner=self)
