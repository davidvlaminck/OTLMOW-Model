# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.RHZModule import RHZModule
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcAfmetingNetwerkelement import DtcAfmetingNetwerkelement, DtcAfmetingNetwerkelementWaarden
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlNetwerkMerk import KlNetwerkMerk
from ...Datatypes.KlNetwerkelemGebruik import KlNetwerkelemGebruik
from ...Datatypes.KlNetwerkelemModelnaam import KlNetwerkelemModelnaam
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkelement(RHZModule, NaampadObject, PuntGeometrie):
    """Toestel,onderdeel van het netwerk zoals een backbone of IP-netwerk,waarop netwerkverbindingen kunnen aangelegd worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#IPBackbone', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#L2AccessStructuur', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsNetwerkECC', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='i')  # i = direction: incoming

        self._afmeting = OTLAttribuut(field=DtcAfmetingNetwerkelement,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.afmeting',
                                      definition='De afmeting van een netwerkelement.',
                                      owner=self)

        self._beschrijvingFabrikant = OTLAttribuut(field=StringField,
                                                   naam='beschrijvingFabrikant',
                                                   label='beschrijving fabrikant',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.beschrijvingFabrikant',
                                                   definition='Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.',
                                                   owner=self)

        self._gebruik = OTLAttribuut(field=KlNetwerkelemGebruik,
                                     naam='gebruik',
                                     label='gebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.gebruik',
                                     definition='Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden.',
                                     owner=self)

        self._ipAddressBeheer = OTLAttribuut(field=DteIPv4Adres,
                                             naam='ipAddressBeheer',
                                             label='IP address beheer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressBeheer',
                                             definition='IP adres van het toestel.',
                                             owner=self)

        self._ipAddressMask = OTLAttribuut(field=DteIPv4Adres,
                                           naam='ipAddressMask',
                                           label='IP address mask',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressMask',
                                           definition='IP adres mask van het toestel.',
                                           owner=self)

        self._ipGateway = OTLAttribuut(field=DteIPv4Adres,
                                       naam='ipGateway',
                                       label='IP gateway',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipGateway',
                                       definition='IP adres van gateway.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlNetwerkMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.merk',
                                  definition='Merk waarmee de fabrikant het netwerkelement identificeert.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlNetwerkelemModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.modelnaam',
                                       definition='Modelnaam waarmee de fabrikant dit type toestel identificeert.',
                                       owner=self)

        self._nSAPAddress = OTLAttribuut(field=StringField,
                                         naam='nSAPAddress',
                                         label='NSAP-address',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.nSAPAddress',
                                         definition='Netwerkadres van deze component.',
                                         owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.',
                                         owner=self)

        self._softwareVersie = OTLAttribuut(field=StringField,
                                            naam='softwareVersie',
                                            label='software versie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.softwareVersie',
                                            definition='Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn.',
                                            owner=self)

        self._telefoonnummer = OTLAttribuut(field=StringField,
                                            naam='telefoonnummer',
                                            label='telefoonnummer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.telefoonnummer',
                                            usagenote='Dit attribuut is alleen verplicht voor netwerkelementen met een eigen telefoonnummer, bv.in DSL gerelateerde installaties.',
                                            definition='Het telefoonnumer van het netwerkelement.',
                                            owner=self)

    @property
    def afmeting(self) -> DtcAfmetingNetwerkelementWaarden:
        """De afmeting van een netwerkelement."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def beschrijvingFabrikant(self) -> str:
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""
        return self._beschrijvingFabrikant.get_waarde()

    @beschrijvingFabrikant.setter
    def beschrijvingFabrikant(self, value):
        self._beschrijvingFabrikant.set_waarde(value, owner=self)

    @property
    def gebruik(self) -> str:
        """Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden."""
        return self._gebruik.get_waarde()

    @gebruik.setter
    def gebruik(self, value):
        self._gebruik.set_waarde(value, owner=self)

    @property
    def ipAddressBeheer(self) -> DteIPv4AdresWaarden:
        """IP adres van het toestel."""
        return self._ipAddressBeheer.get_waarde()

    @ipAddressBeheer.setter
    def ipAddressBeheer(self, value):
        self._ipAddressBeheer.set_waarde(value, owner=self)

    @property
    def ipAddressMask(self) -> DteIPv4AdresWaarden:
        """IP adres mask van het toestel."""
        return self._ipAddressMask.get_waarde()

    @ipAddressMask.setter
    def ipAddressMask(self, value):
        self._ipAddressMask.set_waarde(value, owner=self)

    @property
    def ipGateway(self) -> DteIPv4AdresWaarden:
        """IP adres van gateway."""
        return self._ipGateway.get_waarde()

    @ipGateway.setter
    def ipGateway(self, value):
        self._ipGateway.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk waarmee de fabrikant het netwerkelement identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def nSAPAddress(self) -> str:
        """Netwerkadres van deze component."""
        return self._nSAPAddress.get_waarde()

    @nSAPAddress.setter
    def nSAPAddress(self, value):
        self._nSAPAddress.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def softwareVersie(self) -> str:
        """Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn."""
        return self._softwareVersie.get_waarde()

    @softwareVersie.setter
    def softwareVersie(self, value):
        self._softwareVersie.set_waarde(value, owner=self)

    @property
    def telefoonnummer(self) -> str:
        """Het telefoonnumer van het netwerkelement."""
        return self._telefoonnummer.get_waarde()

    @telefoonnummer.setter
    def telefoonnummer(self, value):
        self._telefoonnummer.set_waarde(value, owner=self)
