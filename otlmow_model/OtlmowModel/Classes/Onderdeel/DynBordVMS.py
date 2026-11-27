# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.Abstracten.ArtikelnummerObject import ArtikelnummerObject
from ...Classes.Abstracten.LEDBord import LEDBord
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlDynBordVMSMerk import KlDynBordVMSMerk
from ...Datatypes.KlDynBordVMSModelnaam import KlDynBordVMSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordVMS(ArtikelnummerObject, LEDBord, NaampadObject):
    """Dynamisch verkeersbord dat gelijktijdig verkeerstekens en teksten kan weergeven op 2 geïntegreerde displays (verkeerstekens uiterst links). Het bord is bevestigd aan een seinbrug en heeft tot doel het verkeer te sturen (over een langer traject) en waarschuwingen en reistijden te tonen. VMS staat voor Variable Message Sign."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DynBordGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._fabricagenummer = OTLAttribuut(field=StringField,
                                             naam='fabricagenummer',
                                             label='fabricagenummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.fabricagenummer',
                                             definition='Een nummer dat referenties bevat naar plannen van het dynamische bord, zowel elektrische als mechanische plannen.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlDynBordVMSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.merk',
                                  definition='Merk van het dynamische bord.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordVMSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.modelnaam',
                                       definition='Modelnaam van het VMS-bord.',
                                       owner=self)

        self._revisienummer = OTLAttribuut(field=StringField,
                                           naam='revisienummer',
                                           label='revisienummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.revisienummer',
                                           definition='Een nummer waarmee het dynamische bord in de DVM centrale gekend staat en gebruikt wordt om aan te sturen.',
                                           owner=self)

    @property
    def fabricagenummer(self) -> str:
        """Een nummer dat referenties bevat naar plannen van het dynamische bord, zowel elektrische als mechanische plannen."""
        return self._fabricagenummer.get_waarde()

    @fabricagenummer.setter
    def fabricagenummer(self, value):
        self._fabricagenummer.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van het dynamische bord."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van het VMS-bord."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def revisienummer(self) -> str:
        """Een nummer waarmee het dynamische bord in de DVM centrale gekend staat en gebruikt wordt om aan te sturen."""
        return self._revisienummer.get_waarde()

    @revisienummer.setter
    def revisienummer(self, value):
        self._revisienummer.set_waarde(value, owner=self)
