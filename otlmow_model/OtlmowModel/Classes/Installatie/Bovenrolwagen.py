# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bovenrolwagen(Geleidingsmechanisme, StaalsoortObject, AIMNaamObject):
    """Dit object is verbonden met de roldeur en bevat wielen die over de bovenste looprails van de constructie rijden, waardoor de deur horizontaal kan bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiel', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen.gewicht',
                                     definition='Het gewicht van de wagen, uitgedrukt in kilogram.',
                                     owner=self)

        self._heeftDeksel = OTLAttribuut(field=BooleanField,
                                         naam='heeftDeksel',
                                         label='heeft deksel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen.heeftDeksel',
                                         definition='Geeft aan of de bovenrolwagen een deksel heeft of niet.',
                                         owner=self)

        self._heeftHijsogen = OTLAttribuut(field=BooleanField,
                                           naam='heeftHijsogen',
                                           label='heeft hijsogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen.heeftHijsogen',
                                           definition='Geeft aan of de bovenrolwagen hijsogen heeft of niet.',
                                           owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de wagen, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def heeftDeksel(self) -> bool:
        """Geeft aan of de bovenrolwagen een deksel heeft of niet."""
        return self._heeftDeksel.get_waarde()

    @heeftDeksel.setter
    def heeftDeksel(self, value):
        self._heeftDeksel.set_waarde(value, owner=self)

    @property
    def heeftHijsogen(self) -> bool:
        """Geeft aan of de bovenrolwagen hijsogen heeft of niet."""
        return self._heeftHijsogen.get_waarde()

    @heeftHijsogen.setter
    def heeftHijsogen(self, value):
        self._heeftHijsogen.set_waarde(value, owner=self)
