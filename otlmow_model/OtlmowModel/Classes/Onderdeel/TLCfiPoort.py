# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.IVRIComponent import IVRIComponent
from ...Datatypes.KlIVRIMerkTLCfi import KlIVRIMerkTLCfi
from ...Datatypes.KlIVRIModelTLCfi import KlIVRIModelTLCfi


# Generated with OTLClassCreator. To modify: extend, do not edit
class TLCfiPoort(IVRIComponent):
    """Functionele software component die een TLC-FI interface aanbiedt waardoor data kan uitgewisseld worden voor intelligente verkeersregelaars."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWOnderdeelVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlIVRIMerkTLCfi,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.merk',
                                  definition='De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIVRIModelTLCfi,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.modelnaam',
                                       definition='De modelnaam/product range van de TLC-fi poort.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de TLC-fi poort."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
