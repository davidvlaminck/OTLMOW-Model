# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlControlepaneelMerk import KlControlepaneelMerk
from ...Datatypes.KlControlepaneelModelnaam import KlControlepaneelModelnaam
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Controlepaneel(SerienummerObject, NaampadObject, PuntGeometrie):
    """Een inrichting voor het besturen van een systeem dat of installatie die zich in de buurt van het controlepaneel bevindt. Een controlepaneel kan onder andere uitgerust zijn met schakelaars,drukknoppen,draaiknoppen,cijfertoetsen,signaallampen,etc."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._merk = OTLAttribuut(field=KlControlepaneelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel.merk',
                                  definition='Het merk van het controlepaneel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlControlepaneelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel.modelnaam',
                                       definition='De modelnaam van het controlepaneel',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het controlepaneel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het controlepaneel"""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
