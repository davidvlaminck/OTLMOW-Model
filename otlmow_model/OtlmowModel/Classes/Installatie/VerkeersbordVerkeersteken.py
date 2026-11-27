# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Verkeersteken import Verkeersteken


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersbordVerkeersteken(Verkeersteken):
    """De voorstelling door middel van een verkeersbord van een aanwijzing ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersteken', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordConcept', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isBeginZone = OTLAttribuut(field=BooleanField,
                                         naam='isBeginZone',
                                         label='is begin van een zone',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken.isBeginZone',
                                         definition='Duidt aan of het verkeersteken het begin van een zone aanduidt.',
                                         owner=self)

        self._isEindeZone = OTLAttribuut(field=BooleanField,
                                         naam='isEindeZone',
                                         label='is einde van een zone',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken.isEindeZone',
                                         definition='Duidt aan of het verkeersteken het einde van een zone aanduidt.',
                                         owner=self)

    @property
    def isBeginZone(self) -> bool:
        """Duidt aan of het verkeersteken het begin van een zone aanduidt."""
        return self._isBeginZone.get_waarde()

    @isBeginZone.setter
    def isBeginZone(self, value):
        self._isBeginZone.set_waarde(value, owner=self)

    @property
    def isEindeZone(self) -> bool:
        """Duidt aan of het verkeersteken het einde van een zone aanduidt."""
        return self._isEindeZone.get_waarde()

    @isEindeZone.setter
    def isEindeZone(self, value):
        self._isEindeZone.set_waarde(value, owner=self)
