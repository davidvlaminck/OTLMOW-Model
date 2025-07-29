# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bovenrolwagen(Geleidingsmechanisme, StaalsoortObject, AIMNaamObject):
    """Dit object is verbonden met de roldeur en bevat wielen die over de bovenste looprails van de constructie rijden, waardoor de deur horizontaal kan bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pendel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiel', direction='i')  # i = direction: incoming

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
