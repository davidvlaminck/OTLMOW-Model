# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElementSpecificatie(VlakGeometrie):
    """De abstracte die de specificaties per element verzameld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElementSpecificatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._elementBreedte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='elementBreedte',
                                            label='element breedte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElementSpecificatie.elementBreedte',
                                            definition='De breedte van één element.',
                                            owner=self)

        self._elementGewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                            naam='elementGewicht',
                                            label='element gewicht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElementSpecificatie.elementGewicht',
                                            definition='Het gewicht van één element.',
                                            owner=self)

        self._elementLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='elementLengte',
                                           label='element lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElementSpecificatie.elementLengte',
                                           definition='De lengte van één element.',
                                           owner=self)

    @property
    def elementBreedte(self) -> KwantWrdInMeterWaarden:
        """De breedte van één element."""
        return self._elementBreedte.get_waarde()

    @elementBreedte.setter
    def elementBreedte(self, value):
        self._elementBreedte.set_waarde(value, owner=self)

    @property
    def elementGewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht van één element."""
        return self._elementGewicht.get_waarde()

    @elementGewicht.setter
    def elementGewicht(self, value):
        self._elementGewicht.set_waarde(value, owner=self)

    @property
    def elementLengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van één element."""
        return self._elementLengte.get_waarde()

    @elementLengte.setter
    def elementLengte(self, value):
        self._elementLengte.set_waarde(value, owner=self)
