# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SlagboomGroep(NaampadObject, PuntGeometrie):
    """Groep voor het groeperen van Slagboom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SlagboomGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom', direction='i')  # i = direction: incoming
