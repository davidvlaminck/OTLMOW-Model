# coding=utf-8
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Soilmixwand(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een cutter soilmixwand (CSM-wand) is een aansluitende kerende wand bestaande uit elkaar overlappende moten in de grond gevormd. Deze heeft een grond- en waterkerende functie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Soilmixwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SoilmixwandElement', direction='i')  # i = direction: incoming
