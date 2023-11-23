# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GecombineerdePut(AIMObject, PuntGeometrie):
    """Alle putrelaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GecombineerdePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
