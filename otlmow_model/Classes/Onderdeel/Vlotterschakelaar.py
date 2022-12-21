# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Niveaumeting import Niveaumeting
from otlmow_model.Datatypes.KlVlotterschakelaarMerk import KlVlotterschakelaarMerk
from otlmow_model.Datatypes.KlVlotterschalelaarModelnaam import KlVlotterschalelaarModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vlotterschakelaar(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv. het waterniveau in een lekwaterput van een kelder of het waterniveau van een waterloop). Een vlotterschakelaar (peilpeer) genereert een stuursignaal door op- en neer te bewegen en contact te maken met discrete contactpunten. De combinatie van verschillende peilperen levert een niveaumeting op.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vlotterschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVlotterschakelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vlotterschakelaar.merk',
                                  definition='Het merk van de vlotterschakeling.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVlotterschalelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vlotterschakelaar.modelnaam',
                                       definition='De modelnaam van de vlotterschakeling.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de vlotterschakeling."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de vlotterschakeling."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
