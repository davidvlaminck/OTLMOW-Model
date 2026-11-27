# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spuier(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een doorvoer in een kunstwerk, bedoeld voor het gecontroleerd afvoeren van water uit de constructie naar een onderliggend afwateringssysteem of open water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.diameter',
                                      definition='De diameter van de spuier.',
                                      owner=self)

        self._heeftOntluchtingsbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftOntluchtingsbuis',
                                                   label='heeft ontluchtingsbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.heeftOntluchtingsbuis',
                                                   definition='Geeft aan of er een ontluchtingsbuis aanwezig is.',
                                                   owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.lengte',
                                    definition='De lengte van de spuier.',
                                    owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de spuier."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def heeftOntluchtingsbuis(self) -> bool:
        """Geeft aan of er een ontluchtingsbuis aanwezig is."""
        return self._heeftOntluchtingsbuis.get_waarde()

    @heeftOntluchtingsbuis.setter
    def heeftOntluchtingsbuis(self, value):
        self._heeftOntluchtingsbuis.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de spuier."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)
