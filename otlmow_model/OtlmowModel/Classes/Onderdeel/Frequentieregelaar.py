# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Frequentieregelaar(NaampadObject, PuntGeometrie):
    """Een elektronisch apparaat dat de snelheid en het koppel van een elektromotor regelt door de frequentie en spanning van de elektrische voeding aan te passen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Frequentieregelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
