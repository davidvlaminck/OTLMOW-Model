# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulppost(NaampadObject, VlakGeometrie):
    """De verzameling van hulpgerelateerde technieken en objecten op een bepaalde plaats,bv.een nis in een tunnel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
