# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handwiel(AIMObject, PuntGeometrie):
    """Een handwiel kan worden gebruikt voor het openen of sluiten van een afsluiter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handwiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter', direction='u')  # u = unidirectional
