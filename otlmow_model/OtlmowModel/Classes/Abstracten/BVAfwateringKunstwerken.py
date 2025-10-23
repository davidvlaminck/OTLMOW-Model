# coding=utf-8
from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class BVAfwateringKunstwerken(ABC):
    """Abstratce om de bevestigingsrelaties van de afwatering te verzamelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BVAfwateringKunstwerken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional

        pass
