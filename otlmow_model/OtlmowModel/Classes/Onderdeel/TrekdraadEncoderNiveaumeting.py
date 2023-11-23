# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Niveaumeting import Niveaumeting
from ...Datatypes.KlTrekdraadEncoderNiveaumetingMerk import KlTrekdraadEncoderNiveaumetingMerk
from ...Datatypes.KlTrekdraadEncoderNiveaumetingModelnaam import KlTrekdraadEncoderNiveaumetingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrekdraadEncoderNiveaumeting(Niveaumeting):
    """Een inrichting voor het bepalen van het peil van een vloeistof (bv het peil van een waterloop, uitgedrukt in meter TAW). Deze inrichting maakt gebruik van een combinatie van vlotter-kabel-encoder. Het resultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrekdraadEncoderNiveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlTrekdraadEncoderNiveaumetingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrekdraadEncoderNiveaumeting.merk',
                                  definition='De merknaam van de trekdraad encoder niveaumeting.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlTrekdraadEncoderNiveaumetingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrekdraadEncoderNiveaumeting.modelnaam',
                                       definition='De modelnaam van de trekdraad encoder niveaumeting.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de trekdraad encoder niveaumeting."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de trekdraad encoder niveaumeting."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
