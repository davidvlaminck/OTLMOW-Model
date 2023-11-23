# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Lager import Lager
from ...Datatypes.KlWentellagerMerk import KlWentellagerMerk
from ...Datatypes.KlWentellagerModelnaam import KlWentellagerModelnaam
from ...Datatypes.KlWentellagerType import KlWentellagerType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wentellager(Lager):
    """Een wentellager of rollend lager is een lager waarin de wrijving wordt verminderd door het gebruiken van rollende elementen tussen de as en de boring. Afhankelijk van de aard en de vorm van het rollend element, spreken we van cilinderlagers, diabololagers, kegellagers, kogellagers, naaldlagers, bollagers of tonlagers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wentellager'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlWentellagerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wentellager.merk',
                                  definition='Het merk van het lager.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWentellagerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wentellager.modelnaam',
                                       definition='De modelnaam volgens de fabrikant van het lager.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlWentellagerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wentellager.type',
                                  definition='Geeft aan welk type wentellager hier gebruikt wordt.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het lager."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam volgens de fabrikant van het lager."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan welk type wentellager hier gebruikt wordt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
