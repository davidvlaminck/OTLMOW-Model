# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Niveaumeting import Niveaumeting
from otlmow_model.Datatypes.KlCapacitieveNiveaumetingMerk import KlCapacitieveNiveaumetingMerk
from otlmow_model.Datatypes.KlCapacitieveNiveaumetingModelnaam import KlCapacitieveNiveaumetingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class CapacitieveNiveaumeting(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv. het waterniveau in een vloeistoftank of lekwaterput van een kelder). Een capacitieve sensor meet de aan- of afwezigheid van een materiaal of vloeistof. Het meest gebruikte type is de driepunts elektrode, hierbij krijgt elke elektrode een eigen grenswaarde, uit de combinatie van de gegeven die de  verschillende elektroden oplevert kan het niveau bepaald worden. Het resultaat wordt omgezet in een uitleesbaar signaal.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CapacitieveNiveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlCapacitieveNiveaumetingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CapacitieveNiveaumeting.merk',
                                  definition='Het merk van de capacitieve niveaumeting.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCapacitieveNiveaumetingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CapacitieveNiveaumeting.modelnaam',
                                       definition='De modelnaam van de capacitieve niveaumeting.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de capacitieve niveaumeting."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de capacitieve niveaumeting."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
