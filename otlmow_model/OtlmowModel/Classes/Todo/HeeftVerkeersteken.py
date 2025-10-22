# coding=utf-8
from ...Classes.Abstracten.DirectioneleRelatiesSV import DirectioneleRelatiesSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftVerkeersteken(DirectioneleRelatiesSV):
    """het verkeersteken dat is opgenomen in het ontwerp"""

    typeURI = 'https://data.vlaanderen.be/ns/todo#heeftVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
