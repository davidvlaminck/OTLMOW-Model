# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagDikte(VlakGeometrie):
    """Abstracte waarmee aan een laag het attribuut dikte wordt toegekend."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagDikte.dikte',
                                   definition='De gemiddelde dikte van een laag in centimeter.',
                                   owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De gemiddelde dikte van een laag in centimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)
