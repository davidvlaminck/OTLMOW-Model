# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Matrixbord(AIMNaamObject, PuntGeometrie):
    """De elektronische displays die in de wanden van een tunnel zijn ingebouwd en die belangrijke informatie aan weggebruikers tonen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Matrixbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
