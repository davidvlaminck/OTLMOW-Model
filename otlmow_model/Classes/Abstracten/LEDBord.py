# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Verkeersbord import Verkeersbord
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.BaseClasses.IntegerField import IntegerField
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDBord(Verkeersbord, AIMNaamObject):
    """Abstracte klasse die de gemeenschappelijke eigenschappen van verschillende types dynamische verkeersborden groepeert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BiFlash')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast')

        self._aantalLichtsensoren = OTLAttribuut(field=IntegerField,
                                                 naam='aantalLichtsensoren',
                                                 label='aantal lichtsensoren',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.aantalLichtsensoren',
                                                 definition='Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten.',
                                                 owner=self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftDeurcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftDeurcontact',
                                              label='heeft deurcontact',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.heeftDeurcontact',
                                              definition='Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm.',
                                              owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.ipAdres',
                                     definition='Het IP netwerkadres van het LEDBord.',
                                     owner=self)

        self._logischeGroepVerkeerscentrum = OTLAttribuut(field=StringField,
                                                          naam='logischeGroepVerkeerscentrum',
                                                          label='logische groep verkeerscentrum',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.logischeGroepVerkeerscentrum',
                                                          definition='Identificator van de logische groep toegekend door het Verkeerscentrum.',
                                                          owner=self)

        self._protocol = OTLAttribuut(field=StringField,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.protocol',
                                      definition='Communicatieprotocol waarmee het LEDBord wordt aangestuurd.',
                                      owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.technischeFiche',
                                             definition='Document met technische informatie over het LEDBord.',
                                             owner=self)

        self._versie = OTLAttribuut(field=StringField,
                                    naam='versie',
                                    label='versie',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.versie',
                                    definition='Versie van het LEDBord.',
                                    owner=self)

    @property
    def aantalLichtsensoren(self) -> int:
        """Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten."""
        return self._aantalLichtsensoren.get_waarde()

    @aantalLichtsensoren.setter
    def aantalLichtsensoren(self, value):
        self._aantalLichtsensoren.set_waarde(value, owner=self)

    @property
    def dnsNaam(self) -> str:
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftDeurcontact(self) -> bool:
        """Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm."""
        return self._heeftDeurcontact.get_waarde()

    @heeftDeurcontact.setter
    def heeftDeurcontact(self, value):
        self._heeftDeurcontact.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Het IP netwerkadres van het LEDBord."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def logischeGroepVerkeerscentrum(self) -> str:
        """Identificator van de logische groep toegekend door het Verkeerscentrum."""
        return self._logischeGroepVerkeerscentrum.get_waarde()

    @logischeGroepVerkeerscentrum.setter
    def logischeGroepVerkeerscentrum(self, value):
        self._logischeGroepVerkeerscentrum.set_waarde(value, owner=self)

    @property
    def protocol(self) -> str:
        """Communicatieprotocol waarmee het LEDBord wordt aangestuurd."""
        return self._protocol.get_waarde()

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document met technische informatie over het LEDBord."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def versie(self) -> str:
        """Versie van het LEDBord."""
        return self._versie.get_waarde()

    @versie.setter
    def versie(self, value):
        self._versie.set_waarde(value, owner=self)
