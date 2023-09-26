# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.Abstracten.Voedingspunt import Voedingspunt
from otlmow_model.Datatypes.KlUPSMerk import KlUPSMerk
from otlmow_model.Datatypes.KlUPSModelnaam import KlUPSModelnaam
from otlmow_model.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from otlmow_model.Datatypes.KwantWrdInHerz import KwantWrdInHerz, KwantWrdInHerzWaarden
from otlmow_model.Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.Datatypes.KwantWrdInkWh import KwantWrdInkWh, KwantWrdInkWhWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class UPS(RHZModule, Voedingspunt, PuntGeometrie):
    """Toestel (Uninterruptible Power Supply = niet onderbreekbare voeding) voor het leveren van elektrische energie van een vastgelegde kwaliteit, onafhankelijk van de beschikbaarheid van een betrouwbare netspanning. Indien het openbare net niet langer bruikbaar is om als energiebron te fungeren, wordt de energievoorziening overgenomen door de accubatterij. Deze zal gedurende een bepaalde tijd, afhankelijk van de capaciteit, de stroomvoorziening verzorgen. De UPS dient om de (minimale) voeding ononderbroken te verzekeren"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AutomatischeOmschakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterijlader')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')

        self._autonomie = OTLAttribuut(field=KwantWrdInkWh,
                                       naam='autonomie',
                                       label='autonomie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.autonomie',
                                       definition='De energie die de UPS kan voorzien aan een installatie voor een zekere tijd.',
                                       owner=self)

        self._maxContinuVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                                naam='maxContinuVermogen',
                                                label='maximaal continu vermogen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxContinuVermogen',
                                                definition='Maximale continu vermogen van de UPS.',
                                                owner=self)

        self._maxPiekVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                             naam='maxPiekVermogen',
                                             label='max piekvermogen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.maxPiekVermogen',
                                             definition='Het maximale piekvermogen van de UPS.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlUPSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.merk',
                                  definition='Merk waarmee de fabrikant de UPS identificeert.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlUPSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.modelnaam',
                                       definition='Modelnaam van de UPS volgens de fabrikant.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.',
                                         owner=self)

        self._uitgangsfrequentie = OTLAttribuut(field=KwantWrdInHerz,
                                                naam='uitgangsfrequentie',
                                                label='uitgangsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.uitgangsfrequentie',
                                                definition='De waarde van de frequentie van de elektriciteit aan de uitgangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul.',
                                                owner=self)

        self._uitgangsstroom = OTLAttribuut(field=KwantWrdInAmpere,
                                            naam='uitgangsstroom',
                                            label='uitgangsstroom',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS.uitgangsstroom',
                                            definition='De waarde van de elektrische stroom aan de uitgangszijde van de omvormer.',
                                            owner=self)

    @property
    def autonomie(self) -> KwantWrdInkWhWaarden:
        """De energie die de UPS kan voorzien aan een installatie voor een zekere tijd."""
        return self._autonomie.get_waarde()

    @autonomie.setter
    def autonomie(self, value):
        self._autonomie.set_waarde(value, owner=self)

    @property
    def maxContinuVermogen(self) -> KwantWrdInWattWaarden:
        """Maximale continu vermogen van de UPS."""
        return self._maxContinuVermogen.get_waarde()

    @maxContinuVermogen.setter
    def maxContinuVermogen(self, value):
        self._maxContinuVermogen.set_waarde(value, owner=self)

    @property
    def maxPiekVermogen(self) -> KwantWrdInWattWaarden:
        """Het maximale piekvermogen van de UPS."""
        return self._maxPiekVermogen.get_waarde()

    @maxPiekVermogen.setter
    def maxPiekVermogen(self, value):
        self._maxPiekVermogen.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk waarmee de fabrikant de UPS identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de UPS volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def uitgangsfrequentie(self) -> KwantWrdInHerzWaarden:
        """De waarde van de frequentie van de elektriciteit aan de uitgangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul."""
        return self._uitgangsfrequentie.get_waarde()

    @uitgangsfrequentie.setter
    def uitgangsfrequentie(self, value):
        self._uitgangsfrequentie.set_waarde(value, owner=self)

    @property
    def uitgangsstroom(self) -> KwantWrdInAmpereWaarden:
        """De waarde van de elektrische stroom aan de uitgangszijde van de omvormer."""
        return self._uitgangsstroom.get_waarde()

    @uitgangsstroom.setter
    def uitgangsstroom(self, value):
        self._uitgangsstroom.set_waarde(value, owner=self)
