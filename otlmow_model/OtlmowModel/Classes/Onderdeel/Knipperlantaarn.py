# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Seinlantaarn import Seinlantaarn
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Knipperlantaarn(Seinlantaarn, NaampadObject):
    """Een lantaarn bestaande uit één of meerdere knipperende oranje-geel verkeerslichten bevestigd op een steun,teneinde de weggebruiker te waarschuwen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Knipperlantaarn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
