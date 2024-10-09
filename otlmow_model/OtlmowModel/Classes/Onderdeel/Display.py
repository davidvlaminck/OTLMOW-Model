# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlDisplayMerk import KlDisplayMerk
from ...Datatypes.KlDisplayModelnaam import KlDisplayModelnaam
from ...Datatypes.KlDisplayType import KlDisplayType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Display(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een display is een elektrisch apparaat, ingebed in een techniek, waarop informatie visueel afgebeeld wordt. en dat kan gebruikt voor sturing van die techniek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Display'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', direction='u')  # u = unidirectional

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
