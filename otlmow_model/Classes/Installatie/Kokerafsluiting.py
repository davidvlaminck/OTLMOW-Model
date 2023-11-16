# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kokerafsluiting(AIMNaamObject, VlakGeometrie):
    """Het geheel van o.a. slagbomen, verkeerslichten en detectielussen in functie van de afsluiting van een koker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
