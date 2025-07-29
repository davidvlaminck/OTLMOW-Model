# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderrolwagen(Geleidingsmechanisme, StaalsoortObject, AIMNaamObject):
    """Dit object is verbonden met de roldeur en bevat wielen die over de onderste looprails van de constructie rijden, waardoor de deur horizontaal kan bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiel', direction='i')  # i = direction: incoming

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
