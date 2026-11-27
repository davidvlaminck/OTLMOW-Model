# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlRelaisMerk import KlRelaisMerk
from ...Datatypes.KlRelaisModelnaam import KlRelaisModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Relais(MotorVermogenskring, NaampadObject):
    """Een door een elektromagneet bediende schakelaar voor het schakelen van kleine vermogens. Ook magneetschakelaar genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
