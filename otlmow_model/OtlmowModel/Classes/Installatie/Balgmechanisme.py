# coding=utf-8
from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Balgmechanisme(Bewegingsmechanisme, AIMObject):
    """Een mechanisme dat de beweegbare waterkerende constructie van een balgstuw beweegt door middel van lucht en/of waterdruk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balgmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Balg', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klemsysteem', direction='i')  # i = direction: incoming
