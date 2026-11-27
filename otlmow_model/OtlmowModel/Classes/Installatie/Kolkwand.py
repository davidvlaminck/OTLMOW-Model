# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kolkwand(AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """De wand van een kolk. Wanden dienen opgesplitst te worden per moot. Elke moot heeft een aparte wand aan beide kanten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftDraineervoorziening = OTLAttribuut(field=BooleanField,
                                                      naam='heeftDraineervoorziening',
                                                      label='heeft draineervoorziening',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkwand.heeftDraineervoorziening',
                                                      definition='Geeft aan of er al dan niet een draineervoorziening aanwezig is.',
                                                      owner=self)

    @property
    def heeftDraineervoorziening(self) -> bool:
        """Geeft aan of er al dan niet een draineervoorziening aanwezig is."""
        return self._heeftDraineervoorziening.get_waarde()

    @heeftDraineervoorziening.setter
    def heeftDraineervoorziening(self, value):
        self._heeftDraineervoorziening.set_waarde(value, owner=self)
