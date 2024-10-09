# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class L2AccessStructuur(NaampadObject, GeenGeometrie):
    """Opstelling die het mogelijk maakt om een techniek direct te koppelen met het IP telematica netwerk. Een L2 access structuur bestaat uit meerdere L2 Switches die met elkaar verbonden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#L2AccessStructuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', direction='i')  # i = direction: incoming
