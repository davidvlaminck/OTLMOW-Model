# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bliksemafleider(AIMNaamObject, PuntGeometrie):
    """Een metalen constructie (meestal een staaf of ring) die zich doorgaans op het hoogste punt van een gebouw bevindt en een laag-impedant pad naar de bodem voorziet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bliksemafleider'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
