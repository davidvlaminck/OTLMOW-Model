# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pompstation(AIMNaamObject, VlakGeometrie):
    """Inrichting voor het oppompen van grond- of oppervlaktewater."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
