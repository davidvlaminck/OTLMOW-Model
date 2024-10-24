# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMotorsturingMerk import KlMotorsturingMerk
from ...Datatypes.KlMotorsturingModelnaam import KlMotorsturingModelnaam
from ...Datatypes.KlMotorsturingType import KlMotorsturingType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Motorsturing(ElektrischComponentennummerObject, MotorVermogenskring, SerienummerObject, AIMNaamObject):
    """Type voor verschillende technieken voor de aansturing van de snelheid (toerental) van een motor."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorsturing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlMotorsturingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorsturing.merk',
                                  definition='Merk van het DC motorsturing component volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlMotorsturingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorsturing.modelnaam',
                                       definition='Naam die de fabrikant zelf geeft aan het model of de uitvoering van het DC motorsturing component.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlMotorsturingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorsturing.type',
                                  definition='Type van de motorsturing volgens de techniek voor aansturing van de gekoppelde motor.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Merk van het DC motorsturing component volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam die de fabrikant zelf geeft aan het model of de uitvoering van het DC motorsturing component."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Type van de motorsturing volgens de techniek voor aansturing van de gekoppelde motor."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
