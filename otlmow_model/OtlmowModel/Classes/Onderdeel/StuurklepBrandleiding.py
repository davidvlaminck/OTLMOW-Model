# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Brandvoorziening import Brandvoorziening
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class StuurklepBrandleiding(Brandvoorziening):
    """Een afsluiter die vanop afstand bediend wordt om te verhinderen dat er water in de leiding blijft staan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional

        self._heeftLeegloopklep = OTLAttribuut(field=BooleanField,
                                               naam='heeftLeegloopklep',
                                               label='heeft leegloopklep',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StuurklepBrandleiding.heeftLeegloopklep',
                                               definition='Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen.',
                                               owner=self)

    @property
    def heeftLeegloopklep(self) -> bool:
        """Voorziet een mogelijkheid om via de klep de brandleiding te laten leeglopen."""
        return self._heeftLeegloopklep.get_waarde()

    @heeftLeegloopklep.setter
    def heeftLeegloopklep(self, value):
        self._heeftLeegloopklep.set_waarde(value, owner=self)
