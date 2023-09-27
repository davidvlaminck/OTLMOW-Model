# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SlagboomarmVerlichting(AIMObject, LijnGeometrie):
    """Verlichting bevestigd aan de slagboomarm om de zichtbaarheid van die arm te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm')
