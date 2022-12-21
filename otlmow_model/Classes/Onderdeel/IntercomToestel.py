# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.Datatypes.KlAudioTransportType import KlAudioTransportType
from otlmow_model.Datatypes.KlIntercomMerk import KlIntercomMerk
from otlmow_model.Datatypes.KlIntercomModelnaam import KlIntercomModelnaam
from otlmow_model.Datatypes.KlIntercomUitvoering import KlIntercomUitvoering
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IntercomToestel(AIMNaamObject, PuntGeometrie):
    """Het toestel dat deel uitmaakt van een intercomsysteem en audio- en/of videocommunicatie tussen twee personen mogelijk maakt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetmicrofoon')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomServer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftCamera = OTLAttribuut(field=BooleanField,
                                         naam='heeftCamera',
                                         label='heeft camera',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.heeftCamera',
                                         definition='Geeft aan of het toestel voorzien is van een camera om naast audio ook video ter verzenden naar een ander toestel in het netwerk.',
                                         owner=self)

        self._heeftVideo = OTLAttribuut(field=BooleanField,
                                        naam='heeftVideo',
                                        label='heeft video',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.heeftVideo',
                                        definition='Geeft aan of communicatie tussen personen al dan niet via video kan verlopen.',
                                        owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.ipAdres',
                                     definition='Het IP-adres van het intercomtoestel.',
                                     owner=self)

        self._isInbouw = OTLAttribuut(field=BooleanField,
                                      naam='isInbouw',
                                      label='is inbouw',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.isInbouw',
                                      definition='Geeft aan of het intercomtoestel een inbouw- of opbouwtoestel is.',
                                      owner=self)

        self._merk = OTLAttribuut(field=KlIntercomMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.merk',
                                  definition='Het merk van het intercomtoestel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIntercomModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.modelnaam',
                                       definition='De modelnaam van het intercomtoestel.',
                                       owner=self)

        self._oproepnummer = OTLAttribuut(field=StringField,
                                          naam='oproepnummer',
                                          label='oproepnummer',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.oproepnummer',
                                          definition='Het nummer dat een gebruiker in een verzendend toestel ingeeft om een verbinding te maken met dit, het ontvangend, toestel.',
                                          owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.technischeFiche',
                                             definition='De technische fiche van het intercomtoestel.',
                                             owner=self)

        self._transportType = OTLAttribuut(field=KlAudioTransportType,
                                           naam='transportType',
                                           label='transporttype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.transportType',
                                           definition='Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem.',
                                           owner=self)

        self._uitvoering = OTLAttribuut(field=KlIntercomUitvoering,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel.uitvoering',
                                        definition='Geeft aan welke functie het toestel vervultin het intercomnetwerk.',
                                        owner=self)

    @property
    def dnsNaam(self) -> str:
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftCamera(self) -> bool:
        """Geeft aan of het toestel voorzien is van een camera om naast audio ook video ter verzenden naar een ander toestel in het netwerk."""
        return self._heeftCamera.get_waarde()

    @heeftCamera.setter
    def heeftCamera(self, value):
        self._heeftCamera.set_waarde(value, owner=self)

    @property
    def heeftVideo(self) -> bool:
        """Geeft aan of communicatie tussen personen al dan niet via video kan verlopen."""
        return self._heeftVideo.get_waarde()

    @heeftVideo.setter
    def heeftVideo(self, value):
        self._heeftVideo.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Het IP-adres van het intercomtoestel."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def isInbouw(self) -> bool:
        """Geeft aan of het intercomtoestel een inbouw- of opbouwtoestel is."""
        return self._isInbouw.get_waarde()

    @isInbouw.setter
    def isInbouw(self, value):
        self._isInbouw.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het intercomtoestel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het intercomtoestel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def oproepnummer(self) -> str:
        """Het nummer dat een gebruiker in een verzendend toestel ingeeft om een verbinding te maken met dit, het ontvangend, toestel."""
        return self._oproepnummer.get_waarde()

    @oproepnummer.setter
    def oproepnummer(self, value):
        self._oproepnummer.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het intercomtoestel."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def transportType(self) -> str:
        """Geeft het type van (video- en) audiotransport aan van het intercomtoestel binnen het intercomsysteem."""
        return self._transportType.get_waarde()

    @transportType.setter
    def transportType(self, value):
        self._transportType.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """Geeft aan welke functie het toestel vervultin het intercomnetwerk."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
