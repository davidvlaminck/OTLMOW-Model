# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PiezometrischeBuis(AIMObject, PuntGeometrie):
    """Een al dan niet permanente buis om waterstanden bij grondverlaging te meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PiezometrischeBuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond')

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PiezometrischeBuis.diepte',
                                    definition='De diepte vanaf maaiveld tot de onderkant van de piezometrische buis in meter.',
                                    owner=self)

    @property
    def diepte(self) -> KwantWrdInMeterWaarden:
        """De diepte vanaf maaiveld tot de onderkant van de piezometrische buis in meter."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)
