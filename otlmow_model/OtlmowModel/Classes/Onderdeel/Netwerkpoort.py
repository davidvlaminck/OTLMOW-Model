# coding=utf-8
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlNetwerkMerk import KlNetwerkMerk
from ...Datatypes.KlNetwerkpoortConfig import KlNetwerkpoortConfig
from ...Datatypes.KlNetwerkpoortGolflengte import KlNetwerkpoortGolflengte
from ...Datatypes.KlNetwerkpoortType import KlNetwerkpoortType
from ...Datatypes.KlNetwerkTechnologie import KlNetwerkTechnologie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkpoort(AIMNaamObject, PuntGeometrie):
    """De ingang van het toestel samen met component die erop zit,bv. SFP of XFP."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkkaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afmetingsensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AlarmModule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DABRepeater', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radiolistener', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WIMDatalogger', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', 'o', '2.9.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IpPowerSwitch', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._beschrijvingFabrikant = OTLAttribuut(field=StringField,
                                                   naam='beschrijvingFabrikant',
                                                   label='beschrijving fabrikant',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.beschrijvingFabrikant',
                                                   definition='Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.',
                                                   owner=self)

        self._code = OTLAttribuut(field=StringField,
                                  naam='code',
                                  label='code',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.code',
                                  definition='Bestelcode van dit toestel of onderdeel bij de fabrikant.',
                                  owner=self)

        self._config = OTLAttribuut(field=KlNetwerkpoortConfig,
                                    naam='config',
                                    label='config',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.config',
                                    definition='Soort verbinding aangeboden aan de klant.',
                                    owner=self)

        self._golflengte = OTLAttribuut(field=KlNetwerkpoortGolflengte,
                                        naam='golflengte',
                                        label='golflengte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.golflengte',
                                        definition='De golflengte waarop deze poort communiceert.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlNetwerkMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.merk',
                                  definition='Merk waarmee de fabrikant de netwerkpoort identificeert.',
                                  owner=self)

        self._nNILANCapaciteit = OTLAttribuut(field=IntegerField,
                                              naam='nNILANCapaciteit',
                                              label='NNI LAN-capaciteit',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.nNILANCapaciteit',
                                              definition='Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort.',
                                              owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.',
                                         owner=self)

        self._technologie = OTLAttribuut(field=KlNetwerkTechnologie,
                                         naam='technologie',
                                         label='technologie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.technologie',
                                         definition='Intern gebruikt netwerk protocol.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlNetwerkpoortType,
                                  naam='type',
                                  label='model',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort.type',
                                  definition='Geeft het soort netwerk interface weer.',
                                  owner=self)

    @property
    def beschrijvingFabrikant(self) -> str:
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""
        return self._beschrijvingFabrikant.get_waarde()

    @beschrijvingFabrikant.setter
    def beschrijvingFabrikant(self, value):
        self._beschrijvingFabrikant.set_waarde(value, owner=self)

    @property
    def code(self) -> str:
        """Bestelcode van dit toestel of onderdeel bij de fabrikant."""
        return self._code.get_waarde()

    @code.setter
    def code(self, value):
        self._code.set_waarde(value, owner=self)

    @property
    def config(self) -> str:
        """Soort verbinding aangeboden aan de klant."""
        return self._config.get_waarde()

    @config.setter
    def config(self, value):
        self._config.set_waarde(value, owner=self)

    @property
    def golflengte(self) -> str:
        """De golflengte waarop deze poort communiceert."""
        return self._golflengte.get_waarde()

    @golflengte.setter
    def golflengte(self, value):
        self._golflengte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk waarmee de fabrikant de netwerkpoort identificeert."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def nNILANCapaciteit(self) -> int:
        """Bandbreedte via deze poort, uitgedrukt in Mb/s, enkel van toepassing indien NNI poort."""
        return self._nNILANCapaciteit.get_waarde()

    @nNILANCapaciteit.setter
    def nNILANCapaciteit(self, value):
        self._nNILANCapaciteit.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def technologie(self) -> str:
        """Intern gebruikt netwerk protocol."""
        return self._technologie.get_waarde()

    @technologie.setter
    def technologie(self, value):
        self._technologie.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Geeft het soort netwerk interface weer."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
