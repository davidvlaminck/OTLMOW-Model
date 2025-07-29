# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MechanischeCilinder(AIMNaamObject, PuntGeometrie):
    """Elektrisch aangedreven actuator waarbij de beweging wordt bewerkstelligd door een inwendig spindelmechanisme."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MechanischeCilinder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Spindelmechanisme', direction='i')  # i = direction: incoming
