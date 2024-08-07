# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VRModuleMetFirmware import VRModuleMetFirmware
from ...Datatypes.KlVrStuurkaartCommunicatieprotocol import KlVrStuurkaartCommunicatieprotocol


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRStuurkaart(VRModuleMetFirmware):
    """Ook wel basissturing genoemd. Dit is de hoofdprocessorkaart van de VRI. Hier wordt het instructieprogramma en het kruispuntprogramma ingeladen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.12.0'

    def __init__(self):
        super().__init__()

        self._communicatieprotocol = OTLAttribuut(field=KlVrStuurkaartCommunicatieprotocol,
                                                  naam='communicatieprotocol',
                                                  label='communicatieprotocol',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRStuurkaart.communicatieprotocol',
                                                  usagenote='Klasse uit gebruik sinds versie 2.12.0 ',
                                                  deprecated_version='2.12.0',
                                                  definition='Gebruikte communicatieprotocol voor de stuurkaart.',
                                                  owner=self)

    @property
    def communicatieprotocol(self) -> str:
        """Gebruikte communicatieprotocol voor de stuurkaart."""
        return self._communicatieprotocol.get_waarde()

    @communicatieprotocol.setter
    def communicatieprotocol(self, value):
        self._communicatieprotocol.set_waarde(value, owner=self)
