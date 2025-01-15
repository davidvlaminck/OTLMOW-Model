# coding=utf-8
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenCaison(BetonnenConstructieElement, Grondkeringen, AIMNaamObject, VlakGeometrie):
    """Kunstwerk in gewapend beton dat dient om af te zinken, groter dan een funderingsput met voornamelijk een grondkerende functie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenCaison'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
