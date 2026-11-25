# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderrolwagen(Geleidingsmechanisme, StaalsoortObject, AIMNaamObject):
    """Dit object is verbonden met de roldeur en bevat wielen die over de onderste looprails van de constructie rijden, waardoor de deur horizontaal kan bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiel', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen.gewicht',
                                     definition='Het gewicht van de wagen, uitgedrukt in kilogram.',
                                     owner=self)

        self._heeftSchraper = OTLAttribuut(field=BooleanField,
                                           naam='heeftSchraper',
                                           label='heeft schraper',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen.heeftSchraper',
                                           definition='Geeft aan of de onderrolwagen een schraper heeft of niet.',
                                           owner=self)

        self._heeftTrekoog = OTLAttribuut(field=BooleanField,
                                          naam='heeftTrekoog',
                                          label='heeft trekoog',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen.heeftTrekoog',
                                          definition='Geeft aan of de onderrolwagen een trekoog heeft of niet.',
                                          owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de wagen, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def heeftSchraper(self) -> bool:
        """Geeft aan of de onderrolwagen een schraper heeft of niet."""
        return self._heeftSchraper.get_waarde()

    @heeftSchraper.setter
    def heeftSchraper(self, value):
        self._heeftSchraper.set_waarde(value, owner=self)

    @property
    def heeftTrekoog(self) -> bool:
        """Geeft aan of de onderrolwagen een trekoog heeft of niet."""
        return self._heeftTrekoog.get_waarde()

    @heeftTrekoog.setter
    def heeftTrekoog(self, value):
        self._heeftTrekoog.set_waarde(value, owner=self)
