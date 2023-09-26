# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.FirmwareObject import FirmwareObject
from otlmow_model.Classes.Abstracten.VerkeersregelaarModule import VerkeersregelaarModule
from otlmow_model.Datatypes.KlVRModuleMetFirmwareMerk import KlVRModuleMetFirmwareMerk
from otlmow_model.Datatypes.KlVRModuleMetFirmwareModelnaam import KlVRModuleMetFirmwareModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRModuleMetFirmware(FirmwareObject, VerkeersregelaarModule):
    """Abstracte voor modules met firmware van een verkeersregelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVRModuleMetFirmwareMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.merk',
                                  definition='Het merk van de VR module met Firmware.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVRModuleMetFirmwareModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRModuleMetFirmware.modelnaam',
                                       definition='De modelnaam/product range van de VR module met Firmware.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de VR module met Firmware."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de VR module met Firmware."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
