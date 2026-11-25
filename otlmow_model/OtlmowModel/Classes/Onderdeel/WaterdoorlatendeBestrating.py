# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bestrating import Bestrating
from ...Datatypes.KlAardWBSS import KlAardWBSS
from ...Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from ...Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from ...Datatypes.KlWBSSType import KlWBSSType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterdoorlatendeBestrating(Bestrating):
    """Betonstraatstenen of betontegels die omwille van hun vormkenmerken (bv. drainageopeningen of verbrede voegen) of betonstructuur (poreus beton met een open korrelopbouw) water doorlaten zoals omschreven in PTV 122."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aard = OTLAttribuut(field=KlAardWBSS,
                                  naam='aard',
                                  label='aard',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard',
                                  definition='Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is.',
                                  owner=self)

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.',
                                                              owner=self)

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking',
                                       definition='Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlWBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type',
                                  definition='Het type van waterdoorlatende betonstraatstenen of betontegels.',
                                  owner=self)

    @property
    def aard(self) -> str:
        """Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is."""
        return self._aard.get_waarde()

    @aard.setter
    def aard(self, value):
        self._aard.set_waarde(value, owner=self)

    @property
    def afmetingVanBestratingselementLxB(self) -> str:
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.get_waarde()

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self) -> str:
        """Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels."""
        return self._afwerking.get_waarde()

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van waterdoorlatende betonstraatstenen of betontegels."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
