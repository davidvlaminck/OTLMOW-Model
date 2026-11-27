# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlRiemMerk import KlRiemMerk
from ...Datatypes.KlRiemType import KlRiemType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riem(AIMNaamObject, PuntGeometrie):
    """Een riem of aandrijfriem zorgt voor het overbrengen van vermogen tussen twee riemschijven. Een riem is samen met een riemschijf en riemspanner onderdeel van een riemoverbrenging."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._merk = OTLAttribuut(field=KlRiemMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem.merk',
                                  definition='Merknaam van de riem.',
                                  owner=self)

        self._onderdeelnummer = OTLAttribuut(field=StringField,
                                             naam='onderdeelnummer',
                                             label='onderdeelnummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem.onderdeelnummer',
                                             definition='Het onderdeelnummer van de riem.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlRiemType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem.type',
                                  definition='Geeft aan welk type riem er gebruikt wordt.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de riem."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def onderdeelnummer(self) -> str:
        """Het onderdeelnummer van de riem."""
        return self._onderdeelnummer.get_waarde()

    @onderdeelnummer.setter
    def onderdeelnummer(self, value):
        self._onderdeelnummer.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Geeft aan welk type riem er gebruikt wordt."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
