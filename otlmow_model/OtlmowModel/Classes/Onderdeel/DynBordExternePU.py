# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.PU import PU
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlDynBordExternePUMerk import KlDynBordExternePUMerk
from ...Datatypes.KlDynBordExternePUModelnaam import KlDynBordExternePUModelnaam
from ...Datatypes.KlMobieleNetwerktechnologie import KlMobieleNetwerktechnologie
from ...Datatypes.KlSimkaarttype import KlSimkaarttype
from ...BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordExternePU(PU, NaampadObject):
    """Lokale stuureenheid van een dynamisch bord of bi-flash, die ook de functie van netwerkmodem vervult. Het betreft dus geen stuureenheid in een serverroom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Z30Groep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BiFlash', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Knipperlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NetwerkModem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._heeftGeintegreerdeModem = OTLAttribuut(field=BooleanField,
                                                     naam='heeftGeintegreerdeModem',
                                                     label='heeft geintegreerde modem',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.heeftGeintegreerdeModem',
                                                     definition='De PU heeft een geïntegreerde modem.',
                                                     owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP Adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.ipAdres',
                                     definition='Netwerkadresgegevens van het element.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlDynBordExternePUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.merk',
                                  definition='Het merk van de externe PU volgens een keuzelijst.',
                                  owner=self)

        self._mobieleNetwerktechnologie = OTLAttribuut(field=KlMobieleNetwerktechnologie,
                                                       naam='mobieleNetwerktechnologie',
                                                       label='mobiele netwerktechnologie',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.mobieleNetwerktechnologie',
                                                       definition='De meest recente mobiele netwerkstandaard waarmee de controller verbinding kan maken. Indien de controller verbonden is met een vast netwerk, dient hier "vast netwerk" gekozen te worden.',
                                                       owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordExternePUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.modelnaam',
                                       definition='De modelnaam van de externe PU volgens een keuzelijst.',
                                       owner=self)

        self._simkaartnummer = OTLAttribuut(field=StringField,
                                            naam='simkaartnummer',
                                            label='simkaartnummer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.simkaartnummer',
                                            definition='Het nummer van de simkaart die aanwezig is.',
                                            owner=self)

        self._simkaarttype = OTLAttribuut(field=KlSimkaarttype,
                                          naam='simkaarttype',
                                          label='simkaarttype',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.simkaarttype',
                                          definition='Het type simkaart dat aanwezig is.',
                                          owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.technischeFiche',
                                             definition='Document met technische informatie over de PU.',
                                             owner=self)

    @property
    def heeftGeintegreerdeModem(self) -> bool:
        """De PU heeft een geïntegreerde modem."""
        return self._heeftGeintegreerdeModem.get_waarde()

    @heeftGeintegreerdeModem.setter
    def heeftGeintegreerdeModem(self, value):
        self._heeftGeintegreerdeModem.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Netwerkadresgegevens van het element."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de externe PU volgens een keuzelijst."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def mobieleNetwerktechnologie(self) -> str:
        """De meest recente mobiele netwerkstandaard waarmee de controller verbinding kan maken. Indien de controller verbonden is met een vast netwerk, dient hier "vast netwerk" gekozen te worden."""
        return self._mobieleNetwerktechnologie.get_waarde()

    @mobieleNetwerktechnologie.setter
    def mobieleNetwerktechnologie(self, value):
        self._mobieleNetwerktechnologie.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de externe PU volgens een keuzelijst."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def simkaartnummer(self) -> str:
        """Het nummer van de simkaart die aanwezig is."""
        return self._simkaartnummer.get_waarde()

    @simkaartnummer.setter
    def simkaartnummer(self, value):
        self._simkaartnummer.set_waarde(value, owner=self)

    @property
    def simkaarttype(self) -> str:
        """Het type simkaart dat aanwezig is."""
        return self._simkaarttype.get_waarde()

    @simkaarttype.setter
    def simkaarttype(self, value):
        self._simkaarttype.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document met technische informatie over de PU."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
