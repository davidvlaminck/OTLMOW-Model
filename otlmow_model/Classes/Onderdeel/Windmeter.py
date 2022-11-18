# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Sensoropstelling import Sensoropstelling
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlWindmeterMerk import KlWindmeterMerk
from otlmow_model.Datatypes.KlWindmeterModelnaam import KlWindmeterModelnaam
from otlmow_model.Datatypes.KlWindmeterType import KlWindmeterType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Windmeter(Sensoropstelling, AIMNaamObject):
    """Een meettoestel dat windsnelheid en/of windrichting meet. Het meetresultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')

        self._merk = OTLAttribuut(field=KlWindmeterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.merk',
                                  definition='Het merk van de windmeter.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWindmeterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.modelnaam',
                                       definition='De mùodelnaam van de windmeter.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlWindmeterType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Windmeter.type',
                                  definition='Het type van windmeter.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de windmeter."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De mùodelnaam van de windmeter."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van windmeter."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
