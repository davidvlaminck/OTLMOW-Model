# coding=utf-8
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandkrans(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een ringvormige constructie die aan één kant voorzien is van vertanding zoals een tandwiel. Deze tanden grijpen in op een tandwiel. Zo kunnen de rotatie en het koppel van het tandwiel overgebracht worden op de tandkrans die aan een bewegend element is bevestigd zoals bijvoorbeeld een draaibrug."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandkrans'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tandkransmechanisme', direction='o')  # o = direction: outgoing
