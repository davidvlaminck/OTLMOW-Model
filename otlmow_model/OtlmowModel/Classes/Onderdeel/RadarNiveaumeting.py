# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Niveaumeting import Niveaumeting
from ...Datatypes.KlRadarNiveaumetingMerk import KlRadarNiveaumetingMerk
from ...Datatypes.KlRadarNiveaumetingModelnaam import KlRadarNiveaumetingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class RadarNiveaumeting(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv het peil van een waterloop, uitgedrukt in meter TAW). De radar meet het tijdsinterval tussen het uitzenden en ontvangen van radiogolven en bepaald hiermee de afstand (hoogte) tot een object (water). Het resultaat wordt omgezet in een uitleesbaar signaal. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RadarNiveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlRadarNiveaumetingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RadarNiveaumeting.merk',
                                  definition='Het merk van de radar niveaumeting.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRadarNiveaumetingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RadarNiveaumeting.modelnaam',
                                       definition='De modelnaam van de rader niveaumeting.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de radar niveaumeting."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de rader niveaumeting."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
