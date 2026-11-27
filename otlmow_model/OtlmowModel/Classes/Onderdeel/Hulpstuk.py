# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BVAfwateringKunstwerken import BVAfwateringKunstwerken
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from ...Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from ...Datatypes.KlHulpstukType import KlHulpstukType
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulpstuk(BVAfwateringKunstwerken, LinkendElement, OmhullendeInrichting, PuntGeometrie):
    """Stukken die zorgen voor verbindingen tussen buizen en/of leidingen om bv. van richting te veranderen,te verlengen,te verlopen van diameter,meerdere buizen op mekaar aan te sluiten,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._inwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='inwendigeDiameter',
                                               label='inwendige diameter',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.inwendigeDiameter',
                                               kardinaliteit_max='*',
                                               definition='De diameter van de binnenzijde van het hulpstuk in millimeter.',
                                               owner=self)

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.materiaal',
                                       definition='Het materiaal waaruit het hulpstuk vervaardigd is.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlHulpstukType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.type',
                                  definition='Het type van het hulpstuk.',
                                  owner=self)

        self._uitwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='uitwendigeDiameter',
                                                label='uitwendige diameter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.uitwendigeDiameter',
                                                kardinaliteit_max='*',
                                                definition='De diameter van de buitenzijde van het hulpstuk in millimeter.',
                                                owner=self)

    @property
    def inwendigeDiameter(self) -> list[KwantWrdInMillimeterWaarden]:
        """De diameter van de binnenzijde van het hulpstuk in millimeter."""
        return self._inwendigeDiameter.get_waarde()

    @inwendigeDiameter.setter
    def inwendigeDiameter(self, value):
        self._inwendigeDiameter.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit het hulpstuk vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van het hulpstuk."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def uitwendigeDiameter(self) -> list[KwantWrdInMillimeterWaarden]:
        """De diameter van de buitenzijde van het hulpstuk in millimeter."""
        return self._uitwendigeDiameter.get_waarde()

    @uitwendigeDiameter.setter
    def uitwendigeDiameter(self, value):
        self._uitwendigeDiameter.set_waarde(value, owner=self)
