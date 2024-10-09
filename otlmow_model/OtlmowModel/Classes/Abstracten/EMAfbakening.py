# coding=utf-8
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class EMAfbakening(AIMNaamObject):
    """Een abstracte klasse voor de Voedt- en Sturing-relaties van allerlei types elektromechansiche afbakening (anders dan de gewone openbare verlichting) in en langs de weg"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMAfbakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
