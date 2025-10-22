# coding=utf-8
from abc import abstractmethod
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DirectioneleRelatiesSV(DirectioneleRelatie):
    """Abstracte als bundeling van de relaties voor Signalisatie Vlaanderen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DirectioneleRelatiesSV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
