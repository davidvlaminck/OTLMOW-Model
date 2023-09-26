# coding=utf-8
from otlmow_model.Classes.Abstracten.LinkendElement import LinkendElement
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ontluchtingsventiel(LinkendElement, PuntGeometrie):
    """Bij het openen van het ventiel hef je de onder- of overdruk op en laat je lucht in- of uitstromen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontluchtingsventiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
