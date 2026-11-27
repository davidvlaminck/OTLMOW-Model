# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.GestandaardiseerdeKantopsluiting import (
    GestandaardiseerdeKantopsluiting,
)
from ...Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from ...Datatypes.DtcTrottoirbandVorm import (
    DtcTrottoirbandVorm,
    DtcTrottoirbandVormWaarden,
)
from ...Datatypes.KlLETrottoirbandWatergreppelType import (
    KlLETrottoirbandWatergreppelType,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandWatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die een trottoirband en een watergreppel combineert in een geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.norm',
                                  definition='De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLETrottoirbandWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde trottoirband_watergreppel.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.vorm',
                                  definition='De vorm van de gestandaardiseerde trottoirband_watergreppel.',
                                  owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van gestandaardiseerde trottoirband_watergreppel."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def vorm(self) -> DtcTrottoirbandVormWaarden:
        """De vorm van de gestandaardiseerde trottoirband_watergreppel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
