# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondanker import Grondanker
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcHellingshoek import DtcHellingshoek, DtcHellingshoekWaarden
from ...Datatypes.KlBeschermingsklasse import KlBeschermingsklasse
from ...Datatypes.KlGroutankerInjectie import KlGroutankerInjectie
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Groutanker(Grondanker, AIMNaamObject):
    """Stalen staaf of strengen die de trekkracht op de grondkering overdraagt op een groutlichaam. Dit lichaam wordt rond het anker onder hoge druk in de bodem gevormd. Door wrijving tussen grout en grond kan de kracht worden overgedragen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional

        self._aanzetpeilwortel = OTLAttribuut(field=KwantWrdInMeterTAW,
                                              naam='aanzetpeilwortel',
                                              label='aanzetpeilwortel',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.aanzetpeilwortel',
                                              definition='Aanzetpeilwortel in mTAW',
                                              owner=self)

        self._beschermingsklasse = OTLAttribuut(field=KlBeschermingsklasse,
                                                naam='beschermingsklasse',
                                                label='beschermingsklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.beschermingsklasse',
                                                definition='Keuzelijst om aan te geven welke beschermingsklasse toegepast is.',
                                                owner=self)

        self._breuklast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                       naam='breuklast',
                                       label='breuklast',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.breuklast',
                                       definition='De breuklast is gelijk aan 1,7 maal de dienstlast in het geval van een tijdelijk anker en gelijk aan tweemaal de dienstlast in het geval van een definitief anker.',
                                       owner=self)

        self._diameterBoorkop = OTLAttribuut(field=KwantWrdInCentimeter,
                                             naam='diameterBoorkop',
                                             label='diameter boorkop',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.diameterBoorkop',
                                             definition='De diameter van de gebruikte boorkop in centimeter.',
                                             owner=self)

        self._dienstlast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                        naam='dienstlast',
                                        label='dienstlast',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.dienstlast',
                                        definition="Ankerkracht in de definitieve toestand onder de karakteristieke combinatie van de belastingen (met inbegrip van de actie 'voorspannen' in het geval van een actief anker) in gebruiksgrenstoestand.",
                                        owner=self)

        self._heeftAnkerkrachtcel = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAnkerkrachtcel',
                                                 label='heeft ankerkrachtcel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.heeftAnkerkrachtcel',
                                                 definition='Aanduiding of er een ankerkrachtcel aanwezig is of niet.',
                                                 owner=self)

        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.hellingshoek',
                                          usagenote='Attribuut uit gebruik sinds versie 2.14.0 ',
                                          deprecated_version='2.14.0',
                                          definition='Hoek van het ingebrachte anker in decimale graden.',
                                          owner=self)

        self._hellingshoekGroutanker = OTLAttribuut(field=DtcHellingshoek,
                                                    naam='hellingshoekGroutanker',
                                                    label='hellingshoek groutanker',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.hellingshoekGroutanker',
                                                    definition='Hoek van het ingebrachte anker in decimale graden alsook de richting.',
                                                    owner=self)

        self._injectiemethode = OTLAttribuut(field=KlGroutankerInjectie,
                                             naam='injectiemethode',
                                             label='injectiemethode',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.injectiemethode',
                                             definition='Keuzelijst om de injectiemogelijkheden aan te duiden.',
                                             owner=self)

        self._isStaafanker = OTLAttribuut(field=BooleanField,
                                          naam='isStaafanker',
                                          label='is staafanker',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.isStaafanker',
                                          definition='Mogelijkheid om aan te geven of het een staafanker is, indien het geen staafanker is, is het een strenganker.',
                                          owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.totaleLengte',
                                          definition='Totale lengte van het groutanker in centimeters.',
                                          owner=self)

        self._voorspankracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                            naam='voorspankracht',
                                            label='voorspankracht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.voorspankracht',
                                            definition='Kracht waarbij het anker vastgezet wordt door de opdrachtnemer na aftrek van de te verwachten spanningsverliezen in het grondanker.',
                                            owner=self)

        self._vrijeLengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                         naam='vrijeLengte',
                                         label='vrije lengte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.vrijeLengte',
                                         definition='Vrije lengte van het anker in centimeter',
                                         owner=self)

        self._wortellengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='wortellengte',
                                          label='wortellengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Groutanker.wortellengte',
                                          definition='De lengte van de wortel in centimeter',
                                          owner=self)

    @property
    def aanzetpeilwortel(self) -> KwantWrdInMeterTAWWaarden:
        """Aanzetpeilwortel in mTAW"""
        return self._aanzetpeilwortel.get_waarde()

    @aanzetpeilwortel.setter
    def aanzetpeilwortel(self, value):
        self._aanzetpeilwortel.set_waarde(value, owner=self)

    @property
    def beschermingsklasse(self) -> str:
        """Keuzelijst om aan te geven welke beschermingsklasse toegepast is."""
        return self._beschermingsklasse.get_waarde()

    @beschermingsklasse.setter
    def beschermingsklasse(self, value):
        self._beschermingsklasse.set_waarde(value, owner=self)

    @property
    def breuklast(self) -> KwantWrdInKiloNewtonWaarden:
        """De breuklast is gelijk aan 1,7 maal de dienstlast in het geval van een tijdelijk anker en gelijk aan tweemaal de dienstlast in het geval van een definitief anker."""
        return self._breuklast.get_waarde()

    @breuklast.setter
    def breuklast(self, value):
        self._breuklast.set_waarde(value, owner=self)

    @property
    def diameterBoorkop(self) -> KwantWrdInCentimeterWaarden:
        """De diameter van de gebruikte boorkop in centimeter."""
        return self._diameterBoorkop.get_waarde()

    @diameterBoorkop.setter
    def diameterBoorkop(self, value):
        self._diameterBoorkop.set_waarde(value, owner=self)

    @property
    def dienstlast(self) -> KwantWrdInKiloNewtonWaarden:
        """Ankerkracht in de definitieve toestand onder de karakteristieke combinatie van de belastingen (met inbegrip van de actie 'voorspannen' in het geval van een actief anker) in gebruiksgrenstoestand."""
        return self._dienstlast.get_waarde()

    @dienstlast.setter
    def dienstlast(self, value):
        self._dienstlast.set_waarde(value, owner=self)

    @property
    def heeftAnkerkrachtcel(self) -> bool:
        """Aanduiding of er een ankerkrachtcel aanwezig is of niet."""
        return self._heeftAnkerkrachtcel.get_waarde()

    @heeftAnkerkrachtcel.setter
    def heeftAnkerkrachtcel(self, value):
        self._heeftAnkerkrachtcel.set_waarde(value, owner=self)

    @property
    def hellingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Hoek van het ingebrachte anker in decimale graden."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self)

    @property
    def hellingshoekGroutanker(self) -> DtcHellingshoekWaarden:
        """Hoek van het ingebrachte anker in decimale graden alsook de richting."""
        return self._hellingshoekGroutanker.get_waarde()

    @hellingshoekGroutanker.setter
    def hellingshoekGroutanker(self, value):
        self._hellingshoekGroutanker.set_waarde(value, owner=self)

    @property
    def injectiemethode(self) -> str:
        """Keuzelijst om de injectiemogelijkheden aan te duiden."""
        return self._injectiemethode.get_waarde()

    @injectiemethode.setter
    def injectiemethode(self, value):
        self._injectiemethode.set_waarde(value, owner=self)

    @property
    def isStaafanker(self) -> bool:
        """Mogelijkheid om aan te geven of het een staafanker is, indien het geen staafanker is, is het een strenganker."""
        return self._isStaafanker.get_waarde()

    @isStaafanker.setter
    def isStaafanker(self, value):
        self._isStaafanker.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInCentimeterWaarden:
        """Totale lengte van het groutanker in centimeters."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def voorspankracht(self) -> KwantWrdInKiloNewtonWaarden:
        """Kracht waarbij het anker vastgezet wordt door de opdrachtnemer na aftrek van de te verwachten spanningsverliezen in het grondanker."""
        return self._voorspankracht.get_waarde()

    @voorspankracht.setter
    def voorspankracht(self, value):
        self._voorspankracht.set_waarde(value, owner=self)

    @property
    def vrijeLengte(self) -> KwantWrdInCentimeterWaarden:
        """Vrije lengte van het anker in centimeter"""
        return self._vrijeLengte.get_waarde()

    @vrijeLengte.setter
    def vrijeLengte(self, value):
        self._vrijeLengte.set_waarde(value, owner=self)

    @property
    def wortellengte(self) -> KwantWrdInCentimeterWaarden:
        """De lengte van de wortel in centimeter"""
        return self._wortellengte.get_waarde()

    @wortellengte.setter
    def wortellengte(self, value):
        self._wortellengte.set_waarde(value, owner=self)
