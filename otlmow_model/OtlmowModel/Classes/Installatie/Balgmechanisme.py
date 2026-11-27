# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Balgmechanisme(Bewegingsmechanisme, AIMObject):
    """Een mechanisme dat de beweegbare waterkerende constructie van een balgstuw beweegt door middel van lucht en/of waterdruk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balgmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Balg', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Houdriem', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
