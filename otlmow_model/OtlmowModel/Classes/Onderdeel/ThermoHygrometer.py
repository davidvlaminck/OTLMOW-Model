# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Sensoropstelling import Sensoropstelling
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlThermoHygrometerMerk import KlThermoHygrometerMerk
from ...Datatypes.KlThermoHygrometerModelnaam import KlThermoHygrometerModelnaam
from ...Datatypes.KlTypeStralingsscherm import KlTypeStralingsscherm


# Generated with OTLClassCreator. To modify: extend, do not edit
class ThermoHygrometer(Sensoropstelling, AIMNaamObject):
    """Een meettoestel dat de temperatuur en vochtigheid van een omgeving of medium meet. Het meetresultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlThermoHygrometerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.merk',
                                  definition='Het merk van de thermo- hygrometer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlThermoHygrometerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.modelnaam',
                                       definition='De modelnaam van de thermo- hygrometer.',
                                       owner=self)

        self._stralingsschermType = OTLAttribuut(field=KlTypeStralingsscherm,
                                                 naam='stralingsschermType',
                                                 label='stralingsscherm type',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer.stralingsschermType',
                                                 definition='Het type van stralingsscherm.',
                                                 owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de thermo- hygrometer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de thermo- hygrometer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def stralingsschermType(self) -> str:
        """Het type van stralingsscherm."""
        return self._stralingsschermType.get_waarde()

    @stralingsschermType.setter
    def stralingsschermType(self, value):
        self._stralingsschermType.set_waarde(value, owner=self)
