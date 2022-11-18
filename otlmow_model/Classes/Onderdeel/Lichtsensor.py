# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Sensoropstelling import Sensoropstelling
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlLichtsensorMerk import KlLichtsensorMerk
from otlmow_model.Datatypes.KlLichtsensorModelnaam import KlLichtsensorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtsensor(Sensoropstelling, AIMNaamObject):
    """Een meettoestel dat wordt gebruikt om de lichtsterkte of illuminantie,voortgebracht door een lichtbron,te meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Sensoropstelling.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')

        self._merk = OTLAttribuut(field=KlLichtsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor.merk',
                                  definition='Het merk van de lichtsensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLichtsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor.modelnaam',
                                       definition='De modelnaam van de lichtsensor.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de lichtsensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de lichtsensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
