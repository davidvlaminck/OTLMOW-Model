# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ArtikelnummerObject import ArtikelnummerObject
from ...Classes.Abstracten.LEDBord import LEDBord
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlDynBordRVMSMerk import KlDynBordRVMSMerk
from ...Datatypes.KlDynBordRVMSModelnaam import KlDynBordRVMSModelnaam
from ...BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordRVMS(ArtikelnummerObject, LEDBord, SerienummerObject, NaampadObject):
    """Dynamisch verkeersbord dat dynamische verkeerstekens en teksten kan afbeelden. RVMS staat voor Road-side Variable Message Signs."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DynBordGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional

        self._fabricagenummer = OTLAttribuut(field=StringField,
                                             naam='fabricagenummer',
                                             label='fabricagenummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.fabricagenummer',
                                             definition='Een nummer dat referenties bevat naar plannen van het dynamische bord, zowel elektrische als mechanische plannen.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlDynBordRVMSMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.merk',
                                  definition='Merk van het dynamische bord.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordRVMSModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.modelnaam',
                                       definition='Modelnaam van het RVMS-bord.',
                                       owner=self)

        self._revisienummer = OTLAttribuut(field=StringField,
                                           naam='revisienummer',
                                           label='revisienummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS.revisienummer',
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
        """Modelnaam van het RVMS-bord."""
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
