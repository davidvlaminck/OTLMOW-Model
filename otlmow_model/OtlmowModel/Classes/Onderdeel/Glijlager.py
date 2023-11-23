# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Lager import Lager
from ...Datatypes.KlGlijlagerMerk import KlGlijlagerMerk
from ...Datatypes.KlGlijlagerModelnaam import KlGlijlagerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Glijlager(Lager):
    """Een machineonderdeel met als functie het toelaten van rotatie of translatie van een as. Bij een glijlager glijdt de as in een vast lager, het verlagen van de wrijving tussen as en lager gebeurt door smering of door het materiaal van het lager."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijlager'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlGlijlagerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijlager.merk',
                                  definition='Het merk van het lager.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlGlijlagerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijlager.modelnaam',
                                       definition='De modelnaam volgens de fabrikant van het lager.',
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
