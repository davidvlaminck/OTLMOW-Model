# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingskeuzeschakelaar(AIMObject, PuntGeometrie):
    """Deze schakelaar biedt de mogelijkheid om handmatig over te schakelen tussen de twee voedingsbronnen om continuïteit van elektrische stroom te behouden, zelfs wanneer de reguliere stroomvoorziening tijdelijk niet beschikbaar is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskeuzeschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='u')  # u = unidirectional
