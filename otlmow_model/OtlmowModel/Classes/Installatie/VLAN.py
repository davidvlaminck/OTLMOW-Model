# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VLAN(NaampadObject, GeenGeometrie):
    """Binnen de L2 access structuur vormt de VLAN een specifieke virtuele LAN. De toepassingen zijn verbonden met een specifieke VLAN. Rechtstreekse communicatie tussen toepassingen is enkel mogelijk indien deze zijn verbonden met dezelfde VLAN."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#L2AccessStructuur', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='i')  # i = direction: incoming

        self._defaultGateway = OTLAttribuut(field=DteIPv4Adres,
                                            naam='defaultGateway',
                                            label='default gateway',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN.defaultGateway',
                                            definition='Het IP adres van de gateway. Binnen een deelnetwerk is de Gateway de toegangspoort tot het ruimere netwerk.',
                                            owner=self)

        self._ipMask = OTLAttribuut(field=DteIPv4Adres,
                                    naam='ipMask',
                                    label='IP mask',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN.ipMask',
                                    definition='Bepaalt welke range van IP adressen beschikbaar zijn in een netwerk.',
                                    owner=self)

        self._ipSubnet = OTLAttribuut(field=DteIPv4Adres,
                                      naam='ipSubnet',
                                      label='IP subnet',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN.ipSubnet',
                                      definition='Identificatie van een IP netwerk binnen een ruimer netwerk.',
                                      owner=self)

        self._vlanId = OTLAttribuut(field=NonNegIntegerField,
                                    naam='vlanId',
                                    label='VLAN identificatienummer',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN.vlanId',
                                    definition='Identificeert een VLAN met een getal tussen 0 en 4095.',
                                    owner=self)

    @property
    def defaultGateway(self) -> DteIPv4AdresWaarden:
        """Het IP adres van de gateway. Binnen een deelnetwerk is de Gateway de toegangspoort tot het ruimere netwerk."""
        return self._defaultGateway.get_waarde()

    @defaultGateway.setter
    def defaultGateway(self, value):
        self._defaultGateway.set_waarde(value, owner=self)

    @property
    def ipMask(self) -> DteIPv4AdresWaarden:
        """Bepaalt welke range van IP adressen beschikbaar zijn in een netwerk."""
        return self._ipMask.get_waarde()

    @ipMask.setter
    def ipMask(self, value):
        self._ipMask.set_waarde(value, owner=self)

    @property
    def ipSubnet(self) -> DteIPv4AdresWaarden:
        """Identificatie van een IP netwerk binnen een ruimer netwerk."""
        return self._ipSubnet.get_waarde()

    @ipSubnet.setter
    def ipSubnet(self, value):
        self._ipSubnet.set_waarde(value, owner=self)

    @property
    def vlanId(self) -> int:
        """Identificeert een VLAN met een getal tussen 0 en 4095."""
        return self._vlanId.get_waarde()

    @vlanId.setter
    def vlanId(self, value):
        self._vlanId.set_waarde(value, owner=self)
