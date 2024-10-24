# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.PompSchroefEnWaaier import PompSchroefEnWaaier
from ...Datatypes.KlWaaierTypeOpstelling import KlWaaierTypeOpstelling
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waaier(PompSchroefEnWaaier, PuntGeometrie):
    """Een mechanische constructie die bestaat uit een aantal schoepen. Deze schoepen brengen de mechanische energie van de aandrijflijn, in de vorm van een roterende beweging, over naar het te verpompen medium. Men spreekt dan van een pomp. In het omgekeerde regime, waarbij er energie wordt overgedragen van de vloeistof op de aandrijflijn, spreekt men van een turbine. Wordt ook wel impeller genoemd. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waaier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._maximaleOpvoerhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='maximaleOpvoerhoogte',
                                                  label='maximale opvoerhoogte',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waaier.maximaleOpvoerhoogte',
                                                  definition='De maximale hoogte die de pomp een vloeistof kan doen bereiken.',
                                                  owner=self)

        self._typeOpstelling = OTLAttribuut(field=KlWaaierTypeOpstelling,
                                            naam='typeOpstelling',
                                            label='type opstelling',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Waaier.typeOpstelling',
                                            definition='Geeft aan van wat voor pomp of turbine de waaierl deel uitmaakt. Bij een axiale pomp, wordt de vloeistof in de richting van de as van de waaier verpompt. Bij een radiale pomp, is er een hoek van 90° tussen de as van de waaierl en de richting waarin het vloeistof wordt verpompt. Bij een gemengde pomp ligt de hoek tussen de as van de waaier en de richting van de stroming van de vloeistof ergens tussen deze twee waarden. Voor turbines geldt een analoge terminologie.',
                                            owner=self)

    @property
    def maximaleOpvoerhoogte(self) -> KwantWrdInMeterWaarden:
        """De maximale hoogte die de pomp een vloeistof kan doen bereiken."""
        return self._maximaleOpvoerhoogte.get_waarde()

    @maximaleOpvoerhoogte.setter
    def maximaleOpvoerhoogte(self, value):
        self._maximaleOpvoerhoogte.set_waarde(value, owner=self)

    @property
    def typeOpstelling(self) -> str:
        """Geeft aan van wat voor pomp of turbine de waaierl deel uitmaakt. Bij een axiale pomp, wordt de vloeistof in de richting van de as van de waaier verpompt. Bij een radiale pomp, is er een hoek van 90° tussen de as van de waaierl en de richting waarin het vloeistof wordt verpompt. Bij een gemengde pomp ligt de hoek tussen de as van de waaier en de richting van de stroming van de vloeistof ergens tussen deze twee waarden. Voor turbines geldt een analoge terminologie."""
        return self._typeOpstelling.get_waarde()

    @typeOpstelling.setter
    def typeOpstelling(self, value):
        self._typeOpstelling.set_waarde(value, owner=self)
