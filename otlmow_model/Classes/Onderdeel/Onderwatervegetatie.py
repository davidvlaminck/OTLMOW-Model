# coding=utf-8
from otlmow_model.Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderwatervegetatie(BegroeidVoorkomen, PuntGeometrie, VlakGeometrie):
    """Vegetatie die zich onder het wateroppervlak bevindt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwatervegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
