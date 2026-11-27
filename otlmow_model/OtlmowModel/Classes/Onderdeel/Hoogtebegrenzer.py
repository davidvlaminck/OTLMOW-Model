# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlHoogtebegrenzerMerk import KlHoogtebegrenzerMerk
from ...Datatypes.KlHoogtebegrenzerModelnaam import KlHoogtebegrenzerModelnaam
from ...Datatypes.KlTypeHoogtebegrenzer import KlTypeHoogtebegrenzer
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoogtebegrenzer(AIMNaamObject, LijnGeometrie):
    """Een object dat de maximale doorrijhoogte voor voertuigen aangeeft om schade aan infrastructuur of voertuigen te voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HoogtebegrenzerInstallatie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._doorrijHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='doorrijHoogte',
                                           label='doorrijhoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer.doorrijHoogte',
                                           definition='De maximale doorrijhoogte in meter dat voor een voertuig beschikbaar is tussen het grondoppervlak en de onderkant van de hoogtebegrenzer.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlHoogtebegrenzerMerk,
                                  naam='merk',
                                  label='hoogtebegrenzer merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer.merk',
                                  definition='Het merk of producent van een hoogtebegrenzer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHoogtebegrenzerModelnaam,
                                       naam='modelnaam',
                                       label='hoogtebegrenzer modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer.modelnaam',
                                       definition='De modelnaam van een hoogtebegrenzer.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer.technischeFiche',
                                             definition='De technische fiche van de hoogtebegrenzer.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlTypeHoogtebegrenzer,
                                  naam='type',
                                  label='type hoogtebegrenzer',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer.type',
                                  definition='Een constructie die de maximale doorrijhoogte voor voertuigen aangeeft om schade aan infrastructuur of voertuigen te voorkomen.',
                                  owner=self)

    @property
    def doorrijHoogte(self) -> KwantWrdInMeterWaarden:
        """De maximale doorrijhoogte in meter dat voor een voertuig beschikbaar is tussen het grondoppervlak en de onderkant van de hoogtebegrenzer."""
        return self._doorrijHoogte.get_waarde()

    @doorrijHoogte.setter
    def doorrijHoogte(self, value):
        self._doorrijHoogte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk of producent van een hoogtebegrenzer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een hoogtebegrenzer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de hoogtebegrenzer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Een constructie die de maximale doorrijhoogte voor voertuigen aangeeft om schade aan infrastructuur of voertuigen te voorkomen."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
