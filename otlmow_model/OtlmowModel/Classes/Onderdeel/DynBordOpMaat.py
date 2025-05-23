# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LEDBord import LEDBord
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlDynBordOpMaatMerk import KlDynBordOpMaatMerk
from ...Datatypes.KlDynBordOpMaatModelnaam import KlDynBordOpMaatModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordOpMaat(LEDBord, NaampadObject):
    """Dynamisch verkeersbord dat niet standaard is; en dus niet is gespecifieerd in SB270."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Matrixbord', direction='o', deprecated='2.10.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlDynBordOpMaatMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.merk',
                                  usagenote='Uit een keuzelijst.',
                                  definition='Merknaam van het dynamisch bord op maat.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDynBordOpMaatModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.modelnaam',
                                       usagenote='Uit een keuzelijst',
                                       definition='Modelnaam van het dynamisch bord op maat.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van het dynamisch bord op maat."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van het dynamisch bord op maat."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
