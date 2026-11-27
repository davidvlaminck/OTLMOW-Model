# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlMateriaalVoegafdichting import KlMateriaalVoegafdichting
from ...Datatypes.KlRichtingVoeg import KlRichtingVoeg
from ...Datatypes.KlUitvoeringVoegafdichting import KlUitvoeringVoegafdichting
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voegafdichting(AIMObject, LijnGeometrie):
    """Een element dat over een voeg tussen constructiedelen wordt aangebracht om deze af te dichten en indringing van water en vuil te voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegafdichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenConstructieObject', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenConstructieObject', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._materiaal = OTLAttribuut(field=KlMateriaalVoegafdichting,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegafdichting.materiaal',
                                       definition='De mogelijke materialen waaruit de voegafdichting kan bestaan.',
                                       owner=self)

        self._richtingVoeg = OTLAttribuut(field=KlRichtingVoeg,
                                          naam='richtingVoeg',
                                          label='richting voeg',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegafdichting.richtingVoeg',
                                          definition='De richting van de voeg waarop de voegafdichting wordt geplaatst.',
                                          owner=self)

        self._uitvoering = OTLAttribuut(field=KlUitvoeringVoegafdichting,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegafdichting.uitvoering',
                                        definition='De mogelijke uitvoeringen van de voegafdichting.',
                                        owner=self)

    @property
    def materiaal(self) -> str:
        """De mogelijke materialen waaruit de voegafdichting kan bestaan."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def richtingVoeg(self) -> str:
        """De richting van de voeg waarop de voegafdichting wordt geplaatst."""
        return self._richtingVoeg.get_waarde()

    @richtingVoeg.setter
    def richtingVoeg(self, value):
        self._richtingVoeg.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """De mogelijke uitvoeringen van de voegafdichting."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
