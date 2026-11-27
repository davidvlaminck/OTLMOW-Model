# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from ...Datatypes.KlEcoOverstaptype import KlEcoOverstaptype
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugkeer(ComplexeGeleiding, LijnGeometrie):
    """Een mogelijkheid om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._typeUitvoering = OTLAttribuut(field=KlEcoOverstaptype,
                                            naam='typeUitvoering',
                                            label='type uitvoering',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer.typeUitvoering',
                                            definition='Het type van terugkeer.',
                                            owner=self)

    @property
    def typeUitvoering(self) -> str:
        """Het type van terugkeer."""
        return self._typeUitvoering.get_waarde()

    @typeUitvoering.setter
    def typeUitvoering(self, value):
        self._typeUitvoering.set_waarde(value, owner=self)
