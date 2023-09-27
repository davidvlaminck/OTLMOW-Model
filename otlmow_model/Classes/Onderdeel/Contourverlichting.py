# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contourverlichting(AIMObject, PuntGeometrie):
    """Groene ledstrip verlichting die de vluchtdeur omrand en zo de visibiliteit van de vluchtdeur en de vluchtweg vergroot."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contourverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur')
