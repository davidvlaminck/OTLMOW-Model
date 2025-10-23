# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VRModuleZFirmware import VRModuleZFirmware
from ...Datatypes.KlVRBatterijCUMerk import KlVRBatterijCUMerk
from ...Datatypes.KlVRBatterijCUModelnaam import KlVRBatterijCUModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBatterijICU(VRModuleZFirmware):
    """Batterij die zorgt dat de primaire melding "spanning afwezig",in het geval van een spanningsuitval,nog kan doorgestuurd worden naar het afstandsbewakingssysteem."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.12.0'

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlVRBatterijCUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.merk',
                                  usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                  deprecated_version='2.12.0',
                                  definition='De merknaam van de VR-batterij ICU.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVRBatterijCUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBatterijICU.modelnaam',
                                       usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                       deprecated_version='2.12.0',
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
