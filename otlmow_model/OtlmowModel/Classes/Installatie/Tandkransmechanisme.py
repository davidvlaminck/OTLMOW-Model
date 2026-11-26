# coding=utf-8
from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandkransmechanisme(Bewegingsmechanisme, AIMObject):
    """Een mechanisme bestaande uit een tandkrans en een aandrijvende tandwielcomponent dat wordt gebruikt om beweging en krachten over te brengen in een cirkelvormige bewegingen, zoals bij draaibruggen of sluisdeuren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tandkransmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandkrans', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel', direction='i')  # i = direction: incoming
