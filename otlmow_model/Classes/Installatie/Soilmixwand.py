# coding=utf-8
from otlmow_model.Classes.Abstracten.Grondkeringen import Grondkeringen
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Soilmixwand(AIMNaamObject, Grondkeringen, LijnGeometrie):
    """Een cutter soilmixwand (CSM-wand) is een aansluitende kerende wand bestaande uit elkaar overlappende moten in de grond gevormd. Deze heeft een grond- en waterkerende functie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Soilmixwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Grondkeringen.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
