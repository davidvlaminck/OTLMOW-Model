# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bebakening import Bebakening
from ...Datatypes.KlWildreflectorDrager import KlWildreflectorDrager
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wildreflector(Bebakening, PuntGeometrie):
    """Een wildreflector is een reflecterend afschrikkingssysteem voor groot en klein wild nabij een weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reflectorpaal', direction='u')  # u = unidirectional

        self._drager = OTLAttribuut(field=KlWildreflectorDrager,
                                    naam='drager',
                                    label='drager',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wildreflector.drager',
                                    definition='De constructie waar de wildreflector is aan bevestigd.',
                                    owner=self)

    @property
    def drager(self) -> str:
        """De constructie waar de wildreflector is aan bevestigd."""
        return self._drager.get_waarde()

    @drager.setter
    def drager(self, value):
        self._drager.set_waarde(value, owner=self)
