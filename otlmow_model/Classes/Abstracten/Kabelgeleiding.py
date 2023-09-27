# coding=utf-8
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.KabelgeleidingEnLeidingBevestiging import KabelgeleidingEnLeidingBevestiging
from otlmow_model.Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgeleiding(KabelgeleidingEnLeidingBevestiging, OmhullendeInrichting, AIMNaamObject):
    """Abstracte voor het groeperen van inrichting met als functie het begeleiden van kabels en leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder')
