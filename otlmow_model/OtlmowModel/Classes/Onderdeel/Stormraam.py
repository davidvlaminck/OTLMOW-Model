# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM, DtcAfmetingBxhInMWaarden
from ...Datatypes.KlMateriaalStormraam import KlMateriaalStormraam
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stormraam(AanhorigheidSluisStuw, AIMNaamObject, LijnGeometrie):
    """Open raamwerk dat aan zeezijde van de afwaartse sluisdeur tegen de sluisdeur geplaatst wordt en vergrendeld door het inschuiven van een spie via verticale cilinder op de deur. Bij voorspelde storm vermijdt dit schade door het voorkomen van klapperen van de afwaartse deuren bij grote stormgolven en wisselende waterdruk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stormraam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxhInM,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stormraam.afmetingen',
                                        definition='De afmetingen, hoogte en breedte, van een stormraam',
                                        owner=self)

        self._materiaalStormraam = OTLAttribuut(field=KlMateriaalStormraam,
                                                naam='materiaalStormraam',
                                                label='materiaal stormraam',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stormraam.materiaalStormraam',
                                                definition='Het gebruikte materiaal voor het stormraam.',
                                                owner=self)

        self._ontwerpwaardeVanNegatieveVerval = OTLAttribuut(field=KwantWrdInMeter,
                                                             naam='ontwerpwaardeVanNegatieveVerval',
                                                             label='ontwerpwaarde van negatieve verval',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stormraam.ontwerpwaardeVanNegatieveVerval',
                                                             definition='De ontwerpwaarde van negatieve verval, uitgedrukt in meter.',
                                                             owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxhInMWaarden:
        """De afmetingen, hoogte en breedte, van een stormraam"""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def materiaalStormraam(self) -> str:
        """Het gebruikte materiaal voor het stormraam."""
        return self._materiaalStormraam.get_waarde()

    @materiaalStormraam.setter
    def materiaalStormraam(self, value):
        self._materiaalStormraam.set_waarde(value, owner=self)

    @property
    def ontwerpwaardeVanNegatieveVerval(self) -> KwantWrdInMeterWaarden:
        """De ontwerpwaarde van negatieve verval, uitgedrukt in meter."""
        return self._ontwerpwaardeVanNegatieveVerval.get_waarde()

    @ontwerpwaardeVanNegatieveVerval.setter
    def ontwerpwaardeVanNegatieveVerval(self, value):
        self._ontwerpwaardeVanNegatieveVerval.set_waarde(value, owner=self)
