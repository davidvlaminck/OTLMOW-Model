# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlContactorMerk import KlContactorMerk
from otlmow_model.Datatypes.KlContactorModelnaam import KlContactorModelnaam
from otlmow_model.Datatypes.KlContactorType import KlContactorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contactor(ElektrischComponentennummerObject, MotorVermogenskring, SerienummerObject, AIMObject):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom')

        self._merk = OTLAttribuut(field=KlContactorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.merk',
                                  definition='Het merk van de contactor volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlContactorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.modelnaam',
                                       definition='De modelnaam van de contactor volgens de fabrikant.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlContactorType,
                                  naam='type',
                                  label='type contactor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor.type',
                                  definition='Geeft aan of het een K of Q contactor betreft.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de contactor volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de contactor volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan of het een K of Q contactor betreft."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
