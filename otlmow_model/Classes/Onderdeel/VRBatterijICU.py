# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.VRModuleZFirmware import VRModuleZFirmware
from otlmow_model.Datatypes.KlVRBatterijCUMerk import KlVRBatterijCUMerk
from otlmow_model.Datatypes.KlVRBatterijCUModelnaam import KlVRBatterijCUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBatterijICU(VRModuleZFirmware):
    """Batterij die zorgt dat de primaire melding "spanning afwezig", in het geval van een spanningsuitval, nog kan doorgestuurd worden naar het afstandsbewakingssysteem."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVRBatterijCUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.merk',
                                  definition='De merknaam van de VR-batterij ICU.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVRBatterijCUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.modelnaam',
                                       definition='De modelnaam van de VR-batterij ICU.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de VR-batterij ICU."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de VR-batterij ICU."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
