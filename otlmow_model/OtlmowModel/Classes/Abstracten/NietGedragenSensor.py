# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.Sensor import Sensor
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietGedragenSensor(Sensor, AIMNaamObject):
    """Abstracte om de eigenschappen en relatie te groeperen voor niet gedragen sensoren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietGedragenSensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
