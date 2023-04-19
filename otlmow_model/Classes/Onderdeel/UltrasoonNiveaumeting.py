# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Niveaumeting import Niveaumeting
from otlmow_model.Datatypes.KlUltrasoonNiveaumetingMerk import KlUltrasoonNiveaumetingMerk
from otlmow_model.Datatypes.KlUltrasoonNiveaumetingModelnaam import KlUltrasoonNiveaumetingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class UltrasoonNiveaumeting(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv. het peil van een waterloop, uitgedrukt in meter TAW). De sensor meet het tijdsinterval tussen het uitzenden en ontvangen van geluidsgolven en bepaald hiermee de afstand (hoogte) tot een object (water). Het resultaat wordt omgezet in een uitleesbaar signaal. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UltrasoonNiveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlUltrasoonNiveaumetingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UltrasoonNiveaumeting.merk',
                                  definition='De merknaam van de ultrasoon niveaumeting.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlUltrasoonNiveaumetingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UltrasoonNiveaumeting.modelnaam',
                                       definition='De modelnaam van de ultrasoon niveaumeting.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de ultrasoon niveaumeting."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de ultrasoon niveaumeting."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
