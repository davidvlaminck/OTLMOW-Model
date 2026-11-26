# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.Waterremmend import Waterremmend


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterremmendeFunctie(Waterremmend):
    """Abstracte voor installaties die waterremmend kunnen zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterremmendeFunctie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
