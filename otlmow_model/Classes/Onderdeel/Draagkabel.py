# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draagkabel(AIMNaamObject, LijnGeometrie):
    """Een kabel opgebouwd uit vele strengen, die gebundeld en omhuld worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
