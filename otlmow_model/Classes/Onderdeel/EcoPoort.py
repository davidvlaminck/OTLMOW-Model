# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from otlmow_model.Datatypes.KlEcoPoorttype import KlEcoPoorttype
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class EcoPoort(ComplexeGeleiding, PuntGeometrie):
    """Een afsluitbare doorgang om mensen toe te laten tot het gebied."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.breedte',
                                     definition='De breedte van de poort in meter.',
                                     owner=self)

        self._poortType = OTLAttribuut(field=KlEcoPoorttype,
                                       naam='poortType',
                                       label='poort type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.poortType',
                                       definition='Bepaling van het type van poort.',
                                       owner=self)

    @property
    def breedte(self) -> KwantWrdInMeterWaarden:
        """De breedte van de poort in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def poortType(self) -> str:
        """Bepaling van het type van poort."""
        return self._poortType.get_waarde()

    @poortType.setter
    def poortType(self, value):
        self._poortType.set_waarde(value, owner=self)
