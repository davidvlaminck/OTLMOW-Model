# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BekledingComponent import BekledingComponent
from ...Datatypes.KlBevestigingsMateriaalBrandwerendeBekleding import (
    KlBevestigingsMateriaalBrandwerendeBekleding,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class AkoestischeBekleding(BekledingComponent):
    """Bekleding die op wanden, plafonds of andere oppervlakken van een constructie wordt aangebracht, met als hoofdfunctie de akoestische prestaties te verbeteren door geluidsweerkaatsing te beperken via geluidsabsorptie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AkoestischeBekleding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bevestigingsmateriaal = OTLAttribuut(field=KlBevestigingsMateriaalBrandwerendeBekleding,
                                                   naam='bevestigingsmateriaal',
                                                   label='bevestigingsmateriaal',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AkoestischeBekleding.bevestigingsmateriaal',
                                                   definition='Het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd.',
                                                   owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AkoestischeBekleding.dikte',
                                   definition='De nominale dikte van de bekleding, uitgedrukt in millimeter.',
                                   owner=self)

    @property
    def bevestigingsmateriaal(self) -> str:
        """Het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd."""
        return self._bevestigingsmateriaal.get_waarde()

    @bevestigingsmateriaal.setter
    def bevestigingsmateriaal(self, value):
        self._bevestigingsmateriaal.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMeterWaarden:
        """De nominale dikte van de bekleding, uitgedrukt in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)
