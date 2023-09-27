# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidingsverlichting(AIMObject, PuntGeometrie, LijnGeometrie):
    """Verlichting die de gestrande weggebruiker begeleiding biedt op handhoogte langs de vluchtroute tot aan een vluchtdeur of tot aan een veilige locatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingsverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
