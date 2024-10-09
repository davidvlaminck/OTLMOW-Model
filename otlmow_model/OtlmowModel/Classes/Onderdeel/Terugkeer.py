# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from ...Datatypes.KlEcoOverstaptype import KlEcoOverstaptype
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Terugkeer(ComplexeGeleiding, LijnGeometrie):
    """Een mogelijkheid om dieren die toch aan de wegkant verzeild zijn geraakt terug naar de veilige kant te laten begeven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Terugkeer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming

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
