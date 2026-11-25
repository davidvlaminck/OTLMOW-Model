# coding=utf-8
from typing import ClassVar

from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Paalmatras(AIMNaamObject, VlakGeometrie):
    """Een funderingsconstructie die wordt gebruikt op slappe bodems, voornamelijk bij de aanleg van wegen en andere infrastructuur. Het combineert (funderings)palen met een dragende matras van gewapend geokunststof en grofkorrelig materiaal, om belastingen efficiënt naar de dieper gelegen stabiele grondlagen over te brengen. De palen dragen de matras, die op zijn beurt de belasting verdeelt en overdraagt aan de palen. Deze aanpak minimaliseert zettingen en verbetert de stabiliteit van de constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Paalmatras'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
