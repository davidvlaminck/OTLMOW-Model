# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlRiemMerk import KlRiemMerk
from ...Datatypes.KlRiemType import KlRiemType
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riem(AIMNaamObject, PuntGeometrie):
    """Een riem of aandrijfriem zorgt voor het overbrengen van vermogen tussen twee riemschijven. Een riem is samen met een riemschijf en riemspanner onderdeel van een riemoverbrenging."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='o')  # o = direction: outgoing

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

    @property
    def type(self) -> str:
        """Geeft aan welk type riem er gebruikt wordt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
