# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.WaterloopRelatie import WaterloopRelatie
from ...Datatypes.KlWaterloopCategorie import KlWaterloopCategorie
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waterloop(WaterloopRelatie, LijnGeometrie):
    """Oorspronkelijk natuurlijke watergeul in het landschap waarin water stroomt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waterloop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._categorie = OTLAttribuut(field=KlWaterloopCategorie,
                                       naam='categorie',
                                       label='categorie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waterloop.categorie',
                                       definition='De categorie betreft een subindeling op basis van het juridisch statuut van de waterloop.',
                                       owner=self)

    @property
    def categorie(self) -> str:
        """De categorie betreft een subindeling op basis van het juridisch statuut van de waterloop."""
        return self._categorie.get_waarde()

    @categorie.setter
    def categorie(self, value):
        self._categorie.set_waarde(value, owner=self)
