# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatierooster(AIMObject, PuntGeometrie):
    """Stuurt de luchtstromen van of naar een ventilator in de gewenste richting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilatierooster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')
