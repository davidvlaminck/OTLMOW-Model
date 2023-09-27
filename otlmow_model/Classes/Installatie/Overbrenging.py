# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overbrenging(AIMNaamObject, PuntGeometrie):
    """Een overbrenging of transmissie brengt een vermogen (bv. van een motor) over op een bewegingsmechanisme. Daarbij kan de snelheid, de kracht en het koppel aangepast worden aan de noden van het bewegingsmechanisme (bv. door gebruik te maken van een tandwielkast)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep')
