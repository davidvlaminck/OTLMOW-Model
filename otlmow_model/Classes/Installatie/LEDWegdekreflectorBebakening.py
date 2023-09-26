# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.EMAfbakening import EMAfbakening
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlKleurReflector import KlKleurReflector
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDWegdekreflectorBebakening(EMAfbakening, LijnGeometrie):
    """De verzameling van op de rijbaan verankerde actieve lichtmodules. De modules hebben als doel de randen van de rijbaan of de grenzen tussen rijstroken te markeren of gevaarlijke plaatsen te signaleren. De verzameling bundelt de actieve reflectoren die hetzelfde obstakel of risico aanduiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalActieveReflectoren = OTLAttribuut(field=NonNegIntegerField,
                                                      naam='aantalActieveReflectoren',
                                                      label='aantal actieve reflectoren',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.aantalActieveReflectoren',
                                                      definition='Het aantal actieve reflectoren in de verzameling van reflectoren die hetzelfde obstakel of risico aangeven.',
                                                      owner=self)

        self._heeftVoedingOpZonneEnergie = OTLAttribuut(field=BooleanField,
                                                        naam='heeftVoedingOpZonneEnergie',
                                                        label='heeft voeding op zonne-energie',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.heeftVoedingOpZonneEnergie',
                                                        definition='Geeft aan dat de verzameling bestaat uit actieve reflectoren met geintegreerde zonnecellen en een batterij die zorgen voor de voeding van de verlichting in de relfector.',
                                                        owner=self)

        self._kleurReflectorAflopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorAflopend',
                                                    label='kleur aflopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.kleurReflectorAflopend',
                                                    definition='De kleur van het niet-actieve deel de reflector stroomafwaarts.',
                                                    owner=self)

        self._kleurReflectorOplopend = OTLAttribuut(field=KlKleurReflector,
                                                    naam='kleurReflectorOplopend',
                                                    label='kleur oplopend',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.kleurReflectorOplopend',
                                                    definition='De kleur van het niet-actieve deel de reflector stroomopwaarts.',
                                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.lengte',
                                    definition='De afstand tussen de eerste en de laatste actieve reflector in de verzameling gevoed door dezelfde stroomkring.',
                                    owner=self)

        self._tussenafstand = OTLAttribuut(field=KwantWrdInCentimeter,
                                           naam='tussenafstand',
                                           label='tussenafstand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDWegdekreflectorBebakening.tussenafstand',
                                           definition='De afstand van middelpunt tot middelpunt tussen twee reflectoren in de verzameling.',
                                           owner=self)

    @property
    def aantalActieveReflectoren(self) -> int:
        """Het aantal actieve reflectoren in de verzameling van reflectoren die hetzelfde obstakel of risico aangeven."""
        return self._aantalActieveReflectoren.get_waarde()

    @aantalActieveReflectoren.setter
    def aantalActieveReflectoren(self, value):
        self._aantalActieveReflectoren.set_waarde(value, owner=self)

    @property
    def heeftVoedingOpZonneEnergie(self) -> bool:
        """Geeft aan dat de verzameling bestaat uit actieve reflectoren met geintegreerde zonnecellen en een batterij die zorgen voor de voeding van de verlichting in de relfector."""
        return self._heeftVoedingOpZonneEnergie.get_waarde()

    @heeftVoedingOpZonneEnergie.setter
    def heeftVoedingOpZonneEnergie(self, value):
        self._heeftVoedingOpZonneEnergie.set_waarde(value, owner=self)

    @property
    def kleurReflectorAflopend(self) -> str:
        """De kleur van het niet-actieve deel de reflector stroomafwaarts."""
        return self._kleurReflectorAflopend.get_waarde()

    @kleurReflectorAflopend.setter
    def kleurReflectorAflopend(self, value):
        self._kleurReflectorAflopend.set_waarde(value, owner=self)

    @property
    def kleurReflectorOplopend(self) -> str:
        """De kleur van het niet-actieve deel de reflector stroomopwaarts."""
        return self._kleurReflectorOplopend.get_waarde()

    @kleurReflectorOplopend.setter
    def kleurReflectorOplopend(self, value):
        self._kleurReflectorOplopend.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de eerste en de laatste actieve reflector in de verzameling gevoed door dezelfde stroomkring."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def tussenafstand(self) -> KwantWrdInCentimeterWaarden:
        """De afstand van middelpunt tot middelpunt tussen twee reflectoren in de verzameling."""
        return self._tussenafstand.get_waarde()

    @tussenafstand.setter
    def tussenafstand(self, value):
        self._tussenafstand.set_waarde(value, owner=self)
