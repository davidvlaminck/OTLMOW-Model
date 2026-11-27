# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlBeheerBoomvorm import KlBeheerBoomvorm
from ...Datatypes.KwantWrdInVierkanteMeter import (
    KwantWrdInVierkanteMeter,
    KwantWrdInVierkanteMeterWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerBoomvorm(AIMObject, VlakGeometrie):
    """Het beheerobject voor de solitaire boom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom', 'i', '2.0.0'),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._beheeroptie = OTLAttribuut(field=KlBeheerBoomvorm,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.beheeroptie',
                                         kardinaliteit_max='*',
                                         definition='Behandelingswijzen van bomen.',
                                         owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerBoomvorm.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen grond rond de boom.',
                                         owner=self)

    @property
    def beheeroptie(self) -> list[str]:
        """Behandelingswijzen van bomen."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de te behandelen grond rond de boom."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
