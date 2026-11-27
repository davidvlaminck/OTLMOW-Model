# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...Classes.Abstracten.KabelgeleidingEnLeidingBevestiging import (
    KabelgeleidingEnLeidingBevestiging,
)
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelgeleiding(KabelgeleidingEnLeidingBevestiging, OmhullendeInrichting, AIMNaamObject):
    """Abstracte voor het groeperen van inrichting met als functie het begeleiden van kabels en leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelgoot', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder', 'o', None),  # o = direction: outgoing
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
