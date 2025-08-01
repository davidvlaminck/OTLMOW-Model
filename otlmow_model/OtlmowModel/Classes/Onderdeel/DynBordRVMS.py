# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LEDBord import LEDBord
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlDynBordRVMSMerk import KlDynBordRVMSMerk
from ...Datatypes.KlDynBordRVMSModelnaam import KlDynBordRVMSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordRVMS(LEDBord, SerienummerObject, NaampadObject):
    """Dynamisch verkeersbord dat dynamische verkeerstekens en teksten kan afbeelden. RVMS staat voor Road-side Variable Message Signs."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRVMS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DynBordGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional

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
