# coding=utf-8
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Loopvloer(AanhorigheidKoker, AIMNaamObject, VlakGeometrie):
    """Een vloer op hoogte die dient om 2 ruimtes op hoogte te verbinden of een niveau te creëren voor inspectie"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte')
