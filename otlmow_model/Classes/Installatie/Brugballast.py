# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugballast(AIMNaamObject, VlakGeometrie):
    """Extra gewicht dat, meestal, geplaatst wordt op het einde van een brugdeel om het brugdeel naar beneden te krijgen. Dit dient om negatieve steunpuntreacties weg te werken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugballast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
