# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.NietGedragenSensor import NietGedragenSensor
from otlmow_model.Datatypes.KlWegdeksensorMerk import KlWegdeksensorMerk
from otlmow_model.Datatypes.KlWegdeksensorModelnaam import KlWegdeksensorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegdeksensor(NietGedragenSensor):
    """Een meettoestel dat wordt gebruikt om verschillende fysische parameters ter hoogte van het wegdek te meten, waaronder de temperatuur op verschillende dieptes, de vochtigheidsgraad van het wegdek en de aanwezigheid van smeltmiddelen op het wegdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdeksensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')

        self._merk = OTLAttribuut(field=KlWegdeksensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdeksensor.merk',
                                  definition='Het merk van de oppervlaktetemperatuursensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWegdeksensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdeksensor.modelnaam',
                                       definition='De modelnaam van de oppervlaktetemperatuursensor.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de oppervlaktetemperatuursensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de oppervlaktetemperatuursensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
