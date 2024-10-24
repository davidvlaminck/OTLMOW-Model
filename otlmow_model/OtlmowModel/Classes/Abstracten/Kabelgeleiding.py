# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.KabelgeleidingEnLeidingBevestiging import KabelgeleidingEnLeidingBevestiging
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgeleiding(KabelgeleidingEnLeidingBevestiging, OmhullendeInrichting, AIMNaamObject):
    """Abstracte voor het groeperen van inrichting met als functie het begeleiden van kabels en leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder', direction='o')  # o = direction: outgoing
