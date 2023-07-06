# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlInbrengmethode import KlInbrengmethode
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenFunderingsprofiel(Funderingspaal):
    """Stalen profiel, bijvoorbeeld een H-profiel, dat wordt gebruikt als fundering of wapening van een fundering. Dit is geen profiel voor een damplank: hiervoor moet 'Stalen damplank' worden gebruikt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand')

        self._aanzetpeilSlot = OTLAttribuut(field=KwantWrdInMeterTAW,
                                            naam='aanzetpeilSlot',
                                            label='aanzetpeil slot',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.aanzetpeilSlot',
                                            definition='Aanzetpeil van het slot.',
                                            owner=self)

        self._inbrengmethode = OTLAttribuut(field=KlInbrengmethode,
                                            naam='inbrengmethode',
                                            label='inbrengmethode',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.inbrengmethode',
                                            definition='Keuzelijst om de inbrengmethode toe te lichten.',
                                            owner=self)

        self._isSlotAanwezig = OTLAttribuut(field=BooleanField,
                                            naam='isSlotAanwezig',
                                            label='is slot aanwezig',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.isSlotAanwezig',
                                            definition='Geeft aan of er al dan niet een slot aanwezig is.',
                                            owner=self)

    @property
    def aanzetpeilSlot(self) -> KwantWrdInMeterTAWWaarden:
        """Aanzetpeil van het slot."""
        return self._aanzetpeilSlot.get_waarde()

    @aanzetpeilSlot.setter
    def aanzetpeilSlot(self, value):
        self._aanzetpeilSlot.set_waarde(value, owner=self)

    @property
    def inbrengmethode(self) -> str:
        """Keuzelijst om de inbrengmethode toe te lichten."""
        return self._inbrengmethode.get_waarde()

    @inbrengmethode.setter
    def inbrengmethode(self, value):
        self._inbrengmethode.set_waarde(value, owner=self)

    @property
    def isSlotAanwezig(self) -> bool:
        """Geeft aan of er al dan niet een slot aanwezig is."""
        return self._isSlotAanwezig.get_waarde()

    @isSlotAanwezig.setter
    def isSlotAanwezig(self, value):
        self._isSlotAanwezig.set_waarde(value, owner=self)
