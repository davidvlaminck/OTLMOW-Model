# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlLuchtkwaliteitOpstellingMerk import KlLuchtkwaliteitOpstellingMerk
from ...Datatypes.KlLuchtkwaliteitOpstellingModelnaam import (
    KlLuchtkwaliteitOpstellingModelnaam,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteittoestel(AIMNaamObject, PuntGeometrie):
    """Abstracte voor attributen van onderdelen van de luchtkwaliteitsensor installatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AkoestischeBekleding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BrandwerendeBekleding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EsthetischeBekleding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie', 'u', None),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._merk = OTLAttribuut(field=KlLuchtkwaliteitOpstellingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.merk',
                                  definition='Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLuchtkwaliteitOpstellingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.modelnaam',
                                       definition='De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
