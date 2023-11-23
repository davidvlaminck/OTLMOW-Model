# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterdoorvoerendeDuiker(AIMNaamObject, LijnGeometrie):
    """Een kokervormige constructie, die is bedoeld om wateren met elkaar te verbinden. Bij een duiker wordt in principe de bodem van de watergang onderbroken, dit in tegenstelling tot een brug."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
