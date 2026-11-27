# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereVerharding import AndereVerharding
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Datatypes.KlUitvoeringsmethodeColloidaalbeton import (
    KlUitvoeringsmethodeColloidaalbeton,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class ColloidaalBeton(AndereVerharding, BetonnenConstructieElement):
    """Betonspecie voor toepassing onder water,waarvan de samenhang is verbeterd door toevoeging van een waterretentiemiddel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftOpenStructuur = OTLAttribuut(field=BooleanField,
                                                naam='heeftOpenStructuur',
                                                label='heeft open structuur',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton.heeftOpenStructuur',
                                                definition='Geeft aan of het colloïdaal beton al dan niet een open structuur heeft.',
                                                owner=self)

        self._uitvoeringsmethodeColloidaalBeton = OTLAttribuut(field=KlUitvoeringsmethodeColloidaalbeton,
                                                               naam='uitvoeringsmethodeColloidaalBeton',
                                                               label='uitvoeringsmethode colloïdaal beton',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton.uitvoeringsmethodeColloidaalBeton',
                                                               definition='De uitvoeringsmethode van het colloïdaal beton.',
                                                               owner=self)

    @property
    def heeftOpenStructuur(self) -> bool:
        """Geeft aan of het colloïdaal beton al dan niet een open structuur heeft."""
        return self._heeftOpenStructuur.get_waarde()

    @heeftOpenStructuur.setter
    def heeftOpenStructuur(self, value):
        self._heeftOpenStructuur.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethodeColloidaalBeton(self) -> str:
        """De uitvoeringsmethode van het colloïdaal beton."""
        return self._uitvoeringsmethodeColloidaalBeton.get_waarde()

    @uitvoeringsmethodeColloidaalBeton.setter
    def uitvoeringsmethodeColloidaalBeton(self, value):
        self._uitvoeringsmethodeColloidaalBeton.set_waarde(value, owner=self)
