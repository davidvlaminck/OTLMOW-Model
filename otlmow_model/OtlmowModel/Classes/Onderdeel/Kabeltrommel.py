# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKilogram import (
    KwantWrdInKilogram,
    KwantWrdInKilogramWaarden,
)
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabeltrommel(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een cilindervormige trommel waarrond een staalkabel wordt gewikkeld om deze te laten bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AsMechanisch', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Staalkabel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelbewegingsmechanisme', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel.breedte',
                                     definition='De breedte van de kabeltrommel.',
                                     owner=self)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel.diameter',
                                      definition='De diameter van de kabeltrommel, uitgedrukt in millimeter.',
                                      owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabeltrommel.gewicht',
                                     definition='Het gewicht, uitgedrukt in kilogram.',
                                     owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van de kabeltrommel."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de kabeltrommel, uitgedrukt in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)
