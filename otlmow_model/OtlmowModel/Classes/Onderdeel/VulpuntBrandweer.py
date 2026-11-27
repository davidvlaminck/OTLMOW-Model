# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Brandvoorziening import Brandvoorziening


# Generated with OTLClassCreator. To modify: extend, do not edit
class VulpuntBrandweer(Brandvoorziening):
    """Klep in de brandleiding waar een vulwagen van de brandweer het debiet van de brandleiding kan verhogen door water toe voegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VulpuntBrandweer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
