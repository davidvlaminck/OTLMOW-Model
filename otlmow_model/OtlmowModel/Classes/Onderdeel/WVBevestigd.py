# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.EMDraagconstructie import EMDraagconstructie
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcAfmetingBxlInMm import (
    DtcAfmetingBxlInMm,
    DtcAfmetingBxlInMmWaarden,
)
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVBevestigd(EMDraagconstructie, NaampadObject, PuntGeometrie):
    """Een draagconstructie,anders dan een WVLichtmast of WVConsole,waarbij verlichting (vlak) tegen een (tunnel)wand,bekleding … kan worden gehangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.afmeting',
                                      definition='De breedte en lengte van de montageplaat in millimeter.',
                                      owner=self)

        self._isDraaibaar = OTLAttribuut(field=BooleanField,
                                         naam='isDraaibaar',
                                         label='is draaibaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.isDraaibaar',
                                         definition='Aanduiding of de bevestiging onder een hoek ingesteld kan worden.',
                                         owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.materiaal',
                                       definition='Het materiaal waaruit de bevestiging bestaat.',
                                       owner=self)

    @property
    def afmeting(self) -> DtcAfmetingBxlInMmWaarden:
        """De breedte en lengte van de montageplaat in millimeter."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def isDraaibaar(self) -> bool:
        """Aanduiding of de bevestiging onder een hoek ingesteld kan worden."""
        return self._isDraaibaar.get_waarde()

    @isDraaibaar.setter
    def isDraaibaar(self, value):
        self._isDraaibaar.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de bevestiging bestaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
