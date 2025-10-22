# coding=utf-8
from ...Classes.Abstracten.DirectioneleRelatiesSV import DirectioneleRelatiesSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class WordtAangeduidDoor(DirectioneleRelatiesSV):
    """Een verkeersteken dat bijdraagt tot de aanduiding van een mobiliteitsmaatregel."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#wordtAangeduidDoor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
