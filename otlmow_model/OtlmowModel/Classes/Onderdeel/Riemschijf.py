# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlRiemschijfMerk import KlRiemschijfMerk
from ...Datatypes.KlRiemschijfModelnaam import KlRiemschijfModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riemschijf(AIMNaamObject, PuntGeometrie):
    """Een riemschijf of poelie wordt op een as bevestigd en brengt het vermogen dat door de as geleverd wordt over op een riem, of omgekeerd. Een riemschijf is samen met een riem en riemspanner onderdeel van een riemoverbrenging."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aandrijfas', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riem', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='o')  # o = direction: outgoing

        self._merk = OTLAttribuut(field=KlRiemschijfMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf.merk',
                                  definition='De merknaam van de riemschijf.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRiemschijfModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemschijf.modelnaam',
                                       definition='De modelnaam van de riemschijf.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de riemschijf."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de riemschijf."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
