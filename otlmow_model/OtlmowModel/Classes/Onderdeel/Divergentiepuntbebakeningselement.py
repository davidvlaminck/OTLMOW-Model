# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlDivergentiepuntbebakeningselementType import (
    KlDivergentiepuntbebakeningselementType,
)
from ...Datatypes.KlFolieType import KlFolieType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Divergentiepuntbebakeningselement(Signalisatie, AIMObject, PuntGeometrie):
    """Een constructie met als doel de zichtbaarheid van het divergentiepunt te vergroten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.folietype',
                                       definition='Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlDivergentiepuntbebakeningselementType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.type',
                                  definition='De vormen van het divergentiepuntbebakeningselement.',
                                  owner=self)

    @property
    def folietype(self) -> str:
        """Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement."""
        return self._folietype.get_waarde()

    @folietype.setter
    def folietype(self, value):
        self._folietype.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """De vormen van het divergentiepuntbebakeningselement."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
