# coding=utf-8
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tegenmateriaal(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een slijtageongevoelig onderdeel dat direct contact maakt met een ander bewegend of stilstaand onderdeel binnen een glijgeleiding. Het betreft het harde deel van de glijgeleiding en dient om krachten over te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tegenmateriaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', direction='o')  # o = direction: outgoing
