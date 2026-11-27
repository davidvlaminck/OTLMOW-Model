# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Loopprofiel(AIMNaamObject, PuntGeometrie):
    """Een dragend profiel dat de werkbreedte van het hijs- en hefwerktuig overspant en dient als rijbaan voor de loopkat, waarbij de uiteinden worden ondersteund door wielen die op de loopbanen rijden of vast bevestigd zijn aan de bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Portiek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HijsEnHefwerktuig', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopkat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._beschikbareLengte = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='beschikbareLengte',
                                               label='beschikbare lengte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopprofiel.beschikbareLengte',
                                               definition='De beschikbare lengte van het loopprofiel waarover een loopkat zich kan verplaatsen.',
                                               owner=self)

    @property
    def beschikbareLengte(self) -> KwantWrdInMeterWaarden:
        """De beschikbare lengte van het loopprofiel waarover een loopkat zich kan verplaatsen."""
        return self._beschikbareLengte.get_waarde()

    @beschikbareLengte.setter
    def beschikbareLengte(self, value):
        self._beschikbareLengte.set_waarde(value, owner=self)
