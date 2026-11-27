# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ArtificieleLaag import ArtificieleLaag
from ...Datatypes.KlAlgBouwklassegroep import KlAlgBouwklassegroep


# Generated with OTLClassCreator. To modify: extend, do not edit
class LaagBouwklasse(ArtificieleLaag):
    """Abstracte waarmee aan een laag het attribuut bouwklasse wordt toegekend."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bouwklasse = OTLAttribuut(field=KlAlgBouwklassegroep,
                                        naam='bouwklasse',
                                        label='bouwklasse',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse.bouwklasse',
                                        definition='Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse.',
                                        owner=self)

    @property
    def bouwklasse(self) -> str:
        """Een maat voor de verkeersbelasting over de volledige levensduur van de laag. De laag is ontworpen volgens de aangeduide bouwklasse."""
        return self._bouwklasse.get_waarde()

    @bouwklasse.setter
    def bouwklasse(self, value):
        self._bouwklasse.set_waarde(value, owner=self)
