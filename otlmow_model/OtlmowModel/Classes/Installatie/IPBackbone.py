# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IPBackbone(NaampadObject, GeenGeometrie):
    """Netwerk dat bestaat uit meerdere L3 switches. Zij verbinden de verschillende L2 access structuren met de datacentres"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#IPBackbone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='i')  # i = direction: incoming
