# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenCaisson(AIMNaamObject, LijnGeometrie):
    """Dit is een samengesteld element bestaande uit twee of meerdere warmgewalste stalen damplanken met Z- of U-vorm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenCaisson'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand')
