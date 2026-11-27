# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangsvoorziening(AIMNaamObject, PuntGeometrie):
    """Een toegangsschouw of ruimte die is ontworpen om personen in staat te stellen componenten van het kunstwerk te bereiken, te inspecteren en eraan te werken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmetingen = OTLAttribuut(field=StringField,
                                        naam='afmetingen',
                                        label='afmetingen toegangsvoorziening',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening.afmetingen',
                                        definition='De afmetingen van de toegangsschouw en ruimte, uitgedrukt in centimeter.',
                                        owner=self)

        self._isVeiligheidsvoorzieningAanwezig = OTLAttribuut(field=BooleanField,
                                                              naam='isVeiligheidsvoorzieningAanwezig',
                                                              label='is veiligheidsvoorziening aanwezig',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening.isVeiligheidsvoorzieningAanwezig',
                                                              definition='Geeft aan of er een veiligheidsvoorziening aanwezig is',
                                                              owner=self)

    @property
    def afmetingen(self) -> str:
        """De afmetingen van de toegangsschouw en ruimte, uitgedrukt in centimeter."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def isVeiligheidsvoorzieningAanwezig(self) -> bool:
        """Geeft aan of er een veiligheidsvoorziening aanwezig is"""
        return self._isVeiligheidsvoorzieningAanwezig.get_waarde()

    @isVeiligheidsvoorzieningAanwezig.setter
    def isVeiligheidsvoorzieningAanwezig(self, value):
        self._isVeiligheidsvoorzieningAanwezig.set_waarde(value, owner=self)
