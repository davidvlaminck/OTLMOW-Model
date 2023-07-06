# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties, DtcConstructiestaalspecificatiesWaarden
from otlmow_model.Datatypes.KlInbrengmethode import KlInbrengmethode
from otlmow_model.Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenBuispaal(Funderingspaal):
    """Volledig op lengte gelast element, meestal door middel van rondnaden, eventueel met inbegrip van de slotprofielen, die door middel van heien of pulsen op diepte wordt gebracht en nadien wordt opgevuld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal'
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AfdekplaatBuispaal')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand')

        self._aanzetpeilSlot = OTLAttribuut(field=KwantWrdInMeterTAW,
                                            naam='aanzetpeilSlot',
                                            label='aanzetpeil slot',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.aanzetpeilSlot',
                                            definition='Het aanzetpeil van het slot.',
                                            owner=self)

        self._heeftPropvorming = OTLAttribuut(field=BooleanField,
                                              naam='heeftPropvorming',
                                              label='heeft propvorming',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.heeftPropvorming',
                                              definition='Geeft aan of er propvorming aanwezig is.',
                                              owner=self)

        self._inbrenglengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='inbrenglengte',
                                           label='inbrenglengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.inbrenglengte',
                                           definition='De lengte voor het inbrengen van de buispaal. Dit is de afstand gemeten, in meter, volgens de as van de buispaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande buispaal, het bovenpeil) en het aanzetpeil (definitief funderingspeil).',
                                           owner=self)

        self._inbrengmethode = OTLAttribuut(field=KlInbrengmethode,
                                            naam='inbrengmethode',
                                            label='inbrengmethode',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.inbrengmethode',
                                            definition='Keuzelijst om aan te geven welke inbrengmethode gebruikt wordt.',
                                            owner=self)

        self._isSlotAanwezig = OTLAttribuut(field=BooleanField,
                                            naam='isSlotAanwezig',
                                            label='is slot aanwezig',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.isSlotAanwezig',
                                            definition='Geeft aan of er een slot aanwezig is of niet.',
                                            owner=self)

        self._leveringsgewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                              naam='leveringsgewicht',
                                              label='leveringsgewicht',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.leveringsgewicht',
                                              definition='Het gewicht van de stalen buispaal bij levering.',
                                              owner=self)

        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal.staalspecificaties',
                                                definition='Eigenschappen van het gebruikte constructiestaal.',
                                                owner=self)

    @property
    def aanzetpeilSlot(self) -> KwantWrdInMeterTAWWaarden:
        """Het aanzetpeil van het slot."""
        return self._aanzetpeilSlot.get_waarde()

    @aanzetpeilSlot.setter
    def aanzetpeilSlot(self, value):
        self._aanzetpeilSlot.set_waarde(value, owner=self)

    @property
    def heeftPropvorming(self) -> bool:
        """Geeft aan of er propvorming aanwezig is."""
        return self._heeftPropvorming.get_waarde()

    @heeftPropvorming.setter
    def heeftPropvorming(self, value):
        self._heeftPropvorming.set_waarde(value, owner=self)

    @property
    def inbrenglengte(self) -> KwantWrdInMeterWaarden:
        """De lengte voor het inbrengen van de buispaal. Dit is de afstand gemeten, in meter, volgens de as van de buispaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande buispaal, het bovenpeil) en het aanzetpeil (definitief funderingspeil)."""
        return self._inbrenglengte.get_waarde()

    @inbrenglengte.setter
    def inbrenglengte(self, value):
        self._inbrenglengte.set_waarde(value, owner=self)

    @property
    def inbrengmethode(self) -> str:
        """Keuzelijst om aan te geven welke inbrengmethode gebruikt wordt."""
        return self._inbrengmethode.get_waarde()

    @inbrengmethode.setter
    def inbrengmethode(self, value):
        self._inbrengmethode.set_waarde(value, owner=self)

    @property
    def isSlotAanwezig(self) -> bool:
        """Geeft aan of er een slot aanwezig is of niet."""
        return self._isSlotAanwezig.get_waarde()

    @isSlotAanwezig.setter
    def isSlotAanwezig(self, value):
        self._isSlotAanwezig.set_waarde(value, owner=self)

    @property
    def leveringsgewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht van de stalen buispaal bij levering."""
        return self._leveringsgewicht.get_waarde()

    @leveringsgewicht.setter
    def leveringsgewicht(self, value):
        self._leveringsgewicht.set_waarde(value, owner=self)

    @property
    def staalspecificaties(self) -> DtcConstructiestaalspecificatiesWaarden:
        """Eigenschappen van het gebruikte constructiestaal."""
        return self._staalspecificaties.get_waarde()

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)
