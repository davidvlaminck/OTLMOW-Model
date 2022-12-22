# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Controller import Controller
from otlmow_model.Datatypes.KlToegangscontrollerMerk import KlToegangscontrollerMerk
from otlmow_model.Datatypes.KlToegangscontrollerModelnaam import KlToegangscontrollerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangscontroller(Controller):
    """Toestel dat een aantal vaste deurmodules voor een toegangscontrolepunt verbindt met een centrale server. Het kan uitgebreid worden met bijkomende deurmodules."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt')

        self._merk = OTLAttribuut(field=KlToegangscontrollerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller.merk',
                                  definition='Merknaam van de toegangscontroller volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlToegangscontrollerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller.modelnaam',
                                       definition='Modelnaam van de toegangscontroller volgens de fabrikant.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de toegangscontroller volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de toegangscontroller volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
