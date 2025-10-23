# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.FirmwareObject import FirmwareObject
from ...Classes.Abstracten.VerkeersregelaarModule import VerkeersregelaarModule
from ...Datatypes.KlVRModuleMetFirmwareMerk import KlVRModuleMetFirmwareMerk
from ...Datatypes.KlVRModuleMetFirmwareModelnaam import KlVRModuleMetFirmwareModelnaam


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
                                  usagenote='Attribuut uit gebruik sinds versie 2.12.0 ',
                                  deprecated_version='2.12.0',
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
