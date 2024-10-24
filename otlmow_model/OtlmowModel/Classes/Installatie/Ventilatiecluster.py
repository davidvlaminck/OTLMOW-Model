# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatiecluster(AIMNaamObject, VlakGeometrie):
    """Een systeem van ventilatoren die samenwerken om de luchtstroom en luchtkwaliteit in een deel van de koker of een specifieke ruimte te reguleren en te verbeteren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ventilatiecluster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerventilatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator', direction='i')  # i = direction: incoming
