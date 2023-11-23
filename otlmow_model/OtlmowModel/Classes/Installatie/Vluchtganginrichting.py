# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtganginrichting(AIMNaamObject, VlakGeometrie):
    """Het geheel van componenten die ontworpen zijn om snel en effectief de evacuatie van mensen te faciliteren in een koker die dienst doet als vluchtgang in geval van een calamiteit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
