# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlDisplayMerk import KlDisplayMerk
from otlmow_model.Datatypes.KlDisplayModelnaam import KlDisplayModelnaam
from otlmow_model.Datatypes.KlDisplayType import KlDisplayType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Display(AIMNaamObject, ElektrischComponentennummerObject, SerienummerObject):
    """Een display is een elektrisch apparaat, ingebed in een techniek, waarop informatie visueel afgebeeld wordt. en dat kan gebruikt voor sturing van die techniek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._isTouchscreen = OTLAttribuut(field=BooleanField,
                                           naam='isTouchscreen',
                                           label='is touchscreen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display.isTouchscreen',
                                           definition='Geeft aan of de display een touchscreen is of niet.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlDisplayMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display.merk',
                                  definition='Het merk van de display.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDisplayModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display.modelnaam',
                                       definition='De modelnaam van de display.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlDisplayType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display.type',
                                  definition='Geeft aan op welk type technologie de display gebaseerd is.',
                                  owner=self)

    @property
    def isTouchscreen(self) -> bool:
        """Geeft aan of de display een touchscreen is of niet."""
        return self._isTouchscreen.get_waarde()

    @isTouchscreen.setter
    def isTouchscreen(self, value):
        self._isTouchscreen.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de display."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de display."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan op welk type technologie de display gebaseerd is."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
