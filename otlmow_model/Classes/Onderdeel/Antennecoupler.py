# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlAntennecouplerMerk import KlAntennecouplerMerk
from otlmow_model.Datatypes.KlAntennecouplerModelnaam import KlAntennecouplerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Antennecoupler(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject):
    """Een element dat toelaat om twee directionele antennes op één coax aan te sluiten. Al doende creëer je één zendontvanger."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')

        self._merk = OTLAttribuut(field=KlAntennecouplerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler.merk',
                                  definition='Het merk van de antennecoupler.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAntennecouplerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler.modelnaam',
                                       definition='De modelnaam van de antennecoupler.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de antennecoupler."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de antennecoupler."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
