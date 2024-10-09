# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlRelaisMerk import KlRelaisMerk
from ...Datatypes.KlRelaisModelnaam import KlRelaisModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Relais(MotorVermogenskring, AIMNaamObject):
    """Een door een elektromagneet bediende schakelaar voor het schakelen van kleine vermogens. Ook magneetschakelaar genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', direction='i')  # i = direction: incoming

        self._merk = OTLAttribuut(field=KlRelaisMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais.merk',
                                  definition='Merk van de relais volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRelaisModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais.modelnaam',
                                       definition='Naam die de fabrikant zelf geeft aan het model of de uitvoering van de relais.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Merk van de relais volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam die de fabrikant zelf geeft aan het model of de uitvoering van de relais."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
