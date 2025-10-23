# coding=utf-8
from ...Classes.Abstracten.DirectioneleRelatiesSV import DirectioneleRelatiesSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsOnderdeelVan(DirectioneleRelatiesSV):
    """Het besluit waarvan het artikel een onderdeel is."""

    typeURI = 'http://purl.org/dc/terms/isPartOf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
