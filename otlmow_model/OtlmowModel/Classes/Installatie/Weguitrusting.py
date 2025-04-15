# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weguitrusting(NaampadObject, PuntGeometrie):
    """Generiek type om alles wat bij de weg hoort in onder te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Weguitrusting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='i')  # i = direction: incoming
