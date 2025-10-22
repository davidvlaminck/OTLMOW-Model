# coding=utf-8
from ...Classes.Abstracten.DirectioneleRelatiesSV import DirectioneleRelatiesSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftMobiliteitsmaatregel(DirectioneleRelatiesSV):
    """Mobiliteitsmaatregel die beschreven staat in het artikel."""

    typeURI = 'https://data.vlaanderen.be/ns/mobiliteit#Artikel.heeftMobiliteitsmaatregel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
