# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.IVRIComponent import IVRIComponent
from ...Datatypes.KlIVRIMerkRIS import KlIVRIMerkRIS
from ...Datatypes.KlIVRIModelRIS import KlIVRIModelRIS


# Generated with OTLClassCreator. To modify: extend, do not edit
class RIS(IVRIComponent):
    """Afkorting van Roadside ITS Station. Functionele software component die een RIS aanbiedt voor de werking van intelligente verkeersregelaars."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWOnderdeelVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isLokaalGehost = OTLAttribuut(field=BooleanField,
                                            naam='isLokaalGehost',
                                            label='is lokaal gehost',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.isLokaalGehost',
                                            definition='Geeft aan of de RIS lokaal wordt gehost in plaats van op een virtuele server.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlIVRIMerkRIS,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.merk',
                                  definition='De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIVRIModelRIS,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.modelnaam',
                                       definition='De modelnaam/product range van de RIS.',
                                       owner=self)

    @property
    def isLokaalGehost(self) -> bool:
        """Geeft aan of de RIS lokaal wordt gehost in plaats van op een virtuele server."""
        return self._isLokaalGehost.get_waarde()

    @isLokaalGehost.setter
    def isLokaalGehost(self, value):
        self._isLokaalGehost.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de RIS."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
