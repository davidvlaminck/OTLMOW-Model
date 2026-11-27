# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.RHZModule import RHZModule
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSignaalControleModuleMerk import KlSignaalControleModuleMerk
from ...Datatypes.KlSignaalControleModuleModelnaam import (
    KlSignaalControleModuleModelnaam,
)
from ...Datatypes.KlSignaalControleModuleType import KlSignaalControleModuleType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignaalControleModule(RHZModule, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een controlemodule dat nagaat of een specifiek (meestal DC-)signaal nog aanwezig is of dat de signaal/ruis-verhouding niet te laag is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._merk = OTLAttribuut(field=KlSignaalControleModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.merk',
                                  definition='Merknaam van de signaal controle module.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSignaalControleModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.modelnaam',
                                       definition='Modelnaam van de signaal controle module.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.technischeFiche',
                                             definition='De technische fiche van de signaal controle module.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlSignaalControleModuleType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.type',
                                  definition='Het type van detectie dat uitgevoerd wordt door de signaal controle module.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de signaal controle module."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de signaal controle module."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de signaal controle module."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van detectie dat uitgevoerd wordt door de signaal controle module."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
