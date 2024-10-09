# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Smeernippel(AIMNaamObject, PuntGeometrie):
    """Een koppelstuk dat een verbinding vormt met de binnenkant van het te smeren systeem. Dit aansluitingspunt laat toe om bijvoorbeeld manueel vet toe te dienen met een vetpomp."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Smeernippel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lagerblok', direction='u')  # u = unidirectional
