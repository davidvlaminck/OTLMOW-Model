# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.PTModuleMetFirmware import PTModuleMetFirmware
from otlmow_model.Datatypes.KlPtKARModemProtocol import KlPtKARModemProtocol


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTKARModem(PTModuleMetFirmware):
    """Modem die KAR signalen, korte afstands radiosignalen, kan ontvangen van de KAR-module die geïnstalleerd is op het openbaar vervoer voertuig. Het voertuig meldt zich zo via virtuele lussen, gedefinieerd op basis van GPS- positie, aan bij de PT regelaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone')

        self._protocolOVVoertuig = OTLAttribuut(field=KlPtKARModemProtocol,
                                                naam='protocolOVVoertuig',
                                                label='protocol OV-voertuig',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem.protocolOVVoertuig',
                                                definition='Beschrijft het protocol dat gebruikt wordt om te communiceren met een OV-voertuig.',
                                                owner=self)

        self._protocolRegelaar = OTLAttribuut(field=KlPtKARModemProtocol,
                                              naam='protocolRegelaar',
                                              label='protocol regelaar',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem.protocolRegelaar',
                                              definition='Beschrijft het protocol dat gebruikt wordt om te communiceren met een regelaar.',
                                              owner=self)

    @property
    def protocolOVVoertuig(self) -> str:
        """Beschrijft het protocol dat gebruikt wordt om te communiceren met een OV-voertuig."""
        return self._protocolOVVoertuig.get_waarde()

    @protocolOVVoertuig.setter
    def protocolOVVoertuig(self, value):
        self._protocolOVVoertuig.set_waarde(value, owner=self)

    @property
    def protocolRegelaar(self) -> str:
        """Beschrijft het protocol dat gebruikt wordt om te communiceren met een regelaar."""
        return self._protocolRegelaar.get_waarde()

    @protocolRegelaar.setter
    def protocolRegelaar(self, value):
        self._protocolRegelaar.set_waarde(value, owner=self)
