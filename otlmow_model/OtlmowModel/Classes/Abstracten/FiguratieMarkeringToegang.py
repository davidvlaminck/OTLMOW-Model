# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...Classes.Abstracten.AOWSType import AOWSType
from ...Classes.Abstracten.Markering import Markering
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class FiguratieMarkeringToegang(AOWSType, Markering, PuntGeometrie):
    """Abstracte als toegang tot de verschillende soorten figuratiemarkeringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FiguratieMarkeringToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering', 'o', None),  # o = direction: outgoing
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
