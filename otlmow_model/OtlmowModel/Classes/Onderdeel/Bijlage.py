# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import (
    AbstracteAanvullendeGeometrie,
)
from ...Datatypes.KlBijlageType import KlBijlageType
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bijlage(AbstracteAanvullendeGeometrie, GeenGeometrie):
    """Een bestand (document,afbeelding,...) dat behoort tot 1 of meerdere assets."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bijlage'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBijlage', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._type = OTLAttribuut(field=KlBijlageType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bijlage.type',
                                  kardinaliteit_max='*',
                                  definition='De typering of categorie van de bijlage.',
                                  owner=self)

    def _get_type(self) -> list[str]:
        """De typering of categorie van de bijlage."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
