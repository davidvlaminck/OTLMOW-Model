# coding=utf-8
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersregelaarModule(AIMNaamObject, PuntGeometrie):
    """Abstracte voor de verschillende modules waaruit een verkeersregelaar opgebouwd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerkeersregelaarModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', direction='u')  # u = unidirectional
