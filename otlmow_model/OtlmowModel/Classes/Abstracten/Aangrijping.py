# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aangrijping(StaalsoortObject, TechnischDocument, PuntGeometrie):
    """Abstracte om attributen en relaties te bundelen voor aangrijping. Een aangrijping maakt de koppeling tussen tussen de actuator en de beweegbare constructive."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Aangrijping'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
