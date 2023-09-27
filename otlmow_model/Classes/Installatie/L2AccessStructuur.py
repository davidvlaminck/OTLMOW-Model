# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class L2AccessStructuur(NaampadObject, GeenGeometrie):
    """Opstelling die het mogelijk maakt om een techniek direct te koppelen met het IP telematica netwerk. Een L2 access structuur bestaat uit meerdere L2 Switches die met elkaar verbonden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#L2AccessStructuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
