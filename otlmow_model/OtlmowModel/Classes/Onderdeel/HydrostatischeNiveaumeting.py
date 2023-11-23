# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Niveaumeting import Niveaumeting
from ...Datatypes.KlHydrostatischeNiveaumetingMerk import KlHydrostatischeNiveaumetingMerk
from ...Datatypes.KlHydrostatischeNiveaumetingModelnaam import KlHydrostatischeNiveaumetingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class HydrostatischeNiveaumeting(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv. het waterniveau in een vloeistoftank of lekwaterput van een kelder). De sensor meet de hydrostatische druk (gewicht) van een vloeistof en bepaalt met deze gegevens het niveau van de vloeistof. Het resultaat wordt omgezet in een uitleesbaar signaal. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HydrostatischeNiveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlHydrostatischeNiveaumetingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HydrostatischeNiveaumeting.merk',
                                  definition='Het merk van de hydrostatische niveaumeting.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHydrostatischeNiveaumetingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HydrostatischeNiveaumeting.modelnaam',
                                       definition='De modelnaam van de hydrostatische niveaumeting.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de hydrostatische niveaumeting."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de hydrostatische niveaumeting."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
