# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabelgeleiding import Kabelgeleiding
from ...Datatypes.KwantWrdInKilogramPerMeter import (
    KwantWrdInKilogramPerMeter,
    KwantWrdInKilogramPerMeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelladder(Kabelgeleiding):
    """Een inrichting die ervoor zorgt dat een kabel beschermd is tegen beschadiging en/of op een gecontroleerde plaats blijft hangen of liggen. De kabelladder is een gerasterde constructie die doet denken aan een ladder, die toelaat om de kabels langs alle kanten te zien. Slechts langs één kant is de toegang tot de kabels fysiek onbelet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._draagvermogen = OTLAttribuut(field=KwantWrdInKilogramPerMeter,
                                           naam='draagvermogen',
                                           label='draagvermogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder.draagvermogen',
                                           definition='Het draagvermogen per meter om kabels te ondersteunen.',
                                           owner=self)

    @property
    def draagvermogen(self) -> KwantWrdInKilogramPerMeterWaarden:
        """Het draagvermogen per meter om kabels te ondersteunen."""
        return self._draagvermogen.get_waarde()

    @draagvermogen.setter
    def draagvermogen(self, value):
        self._draagvermogen.set_waarde(value, owner=self)
