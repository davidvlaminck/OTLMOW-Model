# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.GestandaardiseerdeKantopsluiting import (
    GestandaardiseerdeKantopsluiting,
)
from ...Datatypes.DtcLENorm import DtcLENorm, DtcLENormWaarden
from ...Datatypes.DtcTrottoirbandVorm import (
    DtcTrottoirbandVorm,
    DtcTrottoirbandVormWaarden,
)
from ...Datatypes.KlLEWatergreppelType import KlLEWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting,bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isVerholen = OTLAttribuut(field=BooleanField,
                                        naam='isVerholen',
                                        label='is verholen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.isVerholen',
                                        usagenote='Attribuut uit gebruik sinds versie 2.14.0 ',
                                        deprecated_version='2.14.0',
                                        definition='Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit.',
                                        owner=self)

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.norm',
                                  definition='De gestandaardiseerde watergreppel volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLEWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde watergreppel.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.vorm',
                                  definition='De vorm van de watergreppel.',
                                  owner=self)

    @property
    def isVerholen(self) -> bool:
        """Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit."""
        return self._isVerholen.get_waarde()

    @isVerholen.setter
    def isVerholen(self, value):
        self._isVerholen.set_waarde(value, owner=self)

    @property
    def norm(self) -> DtcLENormWaarden:
        """De gestandaardiseerde watergreppel volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van gestandaardiseerde watergreppel."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def vorm(self) -> DtcTrottoirbandVormWaarden:
        """De vorm van de watergreppel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
