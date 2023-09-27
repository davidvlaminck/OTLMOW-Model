# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Veerooster(ComplexeGeleiding, VlakGeometrie):
    """Een veerooster is een infrastructurele voorziening die is aangebracht in het wegdek om te voorkomen dat vee een gebied binnenkomt of verlaat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster.breedte',
                                     definition='De breedte van het veerooster in meter.',
                                     owner=self)

    @property
    def breedte(self) -> KwantWrdInMeterWaarden:
        """De breedte van het veerooster in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)
