# coding=utf-8
from ...Classes.Abstracten.DirectioneleRelatiesSV import DirectioneleRelatiesSV


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftVoorwaarde(DirectioneleRelatiesSV):
    """Bevat de voorwaarde van de legale verschijningsvorm."""

    typeURI = 'https://data.vlaanderen.be/ns/besluit#heeftVoorwaarde'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
