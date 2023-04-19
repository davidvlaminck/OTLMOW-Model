# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelAarding(LijnGeometrie):
    """Abstracte voor eigenschappen van verschillende types kabel gebruikt voor aardingen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAarding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._buitenmantelDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='buitenmantelDiameter',
                                                  label='buitenmantel diameter',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAarding.buitenmantelDiameter',
                                                  definition='De buitenste afmeting van de kabel in millimeter.',
                                                  owner=self)

    @property
    def buitenmantelDiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitenste afmeting van de kabel in millimeter."""
        return self._buitenmantelDiameter.get_waarde()

    @buitenmantelDiameter.setter
    def buitenmantelDiameter(self, value):
        self._buitenmantelDiameter.set_waarde(value, owner=self)
