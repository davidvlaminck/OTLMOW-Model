# coding=utf-8
from abc import ABC, abstractmethod
from typing import ClassVar


# Generated with OTLClassCreator. To modify: extend, do not edit
class OmhullendeInrichting(ABC):
    """Abstracte voor het groeperen van de relaties voor onderdelen die kabels kunnen omhullen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsCable', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StralendeKabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel', 'o', None),  # o = direction: outgoing
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
