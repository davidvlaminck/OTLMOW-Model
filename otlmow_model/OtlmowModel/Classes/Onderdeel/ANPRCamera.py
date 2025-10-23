# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlANPRMerk import KlANPRMerk
from ...Datatypes.KlANPRModelnaam import KlANPRModelnaam
from ...Datatypes.KlAlgRijrichting import KlAlgRijrichting
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ANPRCamera(AIMNaamObject, PuntGeometrie):
    """Nummerplaatherkenningscamera: een camera die als output de nummerplaat van een voertuig in tekst geeft en een foto van het deel van het voertuig waar de nummerplaat zich bevindt. Afhankelijk van het merk en type gecombineerd met een al dan niet bewegend overzichtsbeeld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.9.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FieldOfView', direction='u', deprecated='2.4.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole', direction='o', deprecated='2.9.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='i', deprecated='2.9.0')  # i = direction: incoming

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.dnsNaam',
                                     usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                     deprecated_version='2.9.0',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftFlits = OTLAttribuut(field=BooleanField,
                                        naam='heeftFlits',
                                        label='heeft flits',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.heeftFlits',
                                        usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                        deprecated_version='2.9.0',
                                        definition='Geeft aan of de camera een externe infrarood flits heeft.',
                                        owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.ipAdres',
                                     usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                     deprecated_version='2.9.0',
                                     definition='IP-adres van de ANPR-camera.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlANPRMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.merk',
                                  usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                  deprecated_version='2.9.0',
                                  definition='Het merk van de ANPR-camera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlANPRModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.modelnaam',
                                       usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                       deprecated_version='2.9.0',
                                       definition='De modelnaam van de ANPR-camera.',
                                       owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.opstelhoogte',
                                          usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                          deprecated_version='2.9.0',
                                          definition='De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is.',
                                          owner=self)

        self._rijrichting = OTLAttribuut(field=KlAlgRijrichting,
                                         naam='rijrichting',
                                         label='rijrichting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.rijrichting',
                                         usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                         deprecated_version='2.9.0',
                                         definition='De rijrichting van de voertuigen die door de camera geregistreerd worden.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.technischeFiche',
                                             usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                             deprecated_version='2.9.0',
                                             definition='Technische fiche van dit element.',
                                             owner=self)

    @property
    def dnsNaam(self) -> str:
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftFlits(self) -> bool:
        """Geeft aan of de camera een externe infrarood flits heeft."""
        return self._heeftFlits.get_waarde()

    @heeftFlits.setter
    def heeftFlits(self, value):
        self._heeftFlits.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """IP-adres van de ANPR-camera."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de ANPR-camera."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de ANPR-camera."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def rijrichting(self) -> str:
        """De rijrichting van de voertuigen die door de camera geregistreerd worden."""
        return self._rijrichting.get_waarde()

    @rijrichting.setter
    def rijrichting(self, value):
        self._rijrichting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche van dit element."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
