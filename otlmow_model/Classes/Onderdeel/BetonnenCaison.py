# coding=utf-8
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Abstracten.Grondkeringen import Grondkeringen
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenCaison(BetonnenConstructieElement, Grondkeringen, AIMNaamObject, VlakGeometrie):
    """Kunstwerk in gewapend beton dat dient om af te zinken, groter dan een funderingsput met voornamelijk een grondkerende functie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenCaison'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
