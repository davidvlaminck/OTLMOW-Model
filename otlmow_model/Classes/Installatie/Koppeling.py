# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Koppeling(AIMNaamObject, PuntGeometrie):
    """Een koppeling is een machineonderdeel dat wordt gebruikt om vermogen (rotatie en koppel) over te brengen van een aandrijvende as naar een aangedreven as."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koppeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep')
