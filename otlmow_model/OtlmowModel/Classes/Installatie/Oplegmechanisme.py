# coding=utf-8
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegmechanisme(Geleidingsmechanisme, AIMObject):
    """Mechanisme dat de overdracht van krachten tussen brugdek en onderbouw toelaat en regelt, terwijl gecontroleerde vervormingen zoals rotatie, translatie of uitzetting mogelijk blijven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagstoel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging', direction='i')  # i = direction: incoming
