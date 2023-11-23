# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lensplaat(AIMObject, GeenGeometrie):
    """Afsluitplaat van de camerakast."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lensplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
