# coding=utf-8
from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stangenmechanisme(Bewegingsmechanisme, AIMObject):
    """Een mechanisme waarbij een kruk en een stang samenwerken om een lineaire beweging om te zetten in een roterende beweging of omgekeerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stangenmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kruk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stang', direction='i')  # i = direction: incoming
