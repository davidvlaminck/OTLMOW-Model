# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from ...Datatypes.KlInbrengmethode import KlInbrengmethode
from ...Datatypes.KwantWrdInMeterTAW import (
    KwantWrdInMeterTAW,
    KwantWrdInMeterTAWWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenFunderingsprofiel(Funderingspaal, LijnGeometrie):
    """Stalen profiel, bijvoorbeeld een H-profiel, dat wordt gebruikt als fundering of wapening van een fundering. Dit is geen profiel voor een damwand: hiervoor moet 'Stalen damplank' worden gebruikt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StandaardStalenProfiel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aanzetpeilSlot = OTLAttribuut(field=KwantWrdInMeterTAW,
                                            naam='aanzetpeilSlot',
                                            label='aanzetpeil slot',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.aanzetpeilSlot',
                                            definition='Aanzetpeil van het slot.',
                                            owner=self)

        self._inbrengmethode = OTLAttribuut(field=KlInbrengmethode,
                                            naam='inbrengmethode',
                                            label='inbrengmethode',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.inbrengmethode',
                                            definition='Keuzelijst om de inbrengmethode toe te lichten.',
                                            owner=self)

        self._isSlotAanwezig = OTLAttribuut(field=BooleanField,
                                            naam='isSlotAanwezig',
                                            label='is slot aanwezig',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel.isSlotAanwezig',
                                            definition='Geeft aan of er al dan niet een slot aanwezig is.',
                                            owner=self)

    @property
    def aanzetpeilSlot(self) -> KwantWrdInMeterTAWWaarden:
        """Aanzetpeil van het slot."""
        return self._aanzetpeilSlot.get_waarde()

    @aanzetpeilSlot.setter
    def aanzetpeilSlot(self, value):
        self._aanzetpeilSlot.set_waarde(value, owner=self)

    @property
    def inbrengmethode(self) -> str:
        """Keuzelijst om de inbrengmethode toe te lichten."""
        return self._inbrengmethode.get_waarde()

    @inbrengmethode.setter
    def inbrengmethode(self, value):
        self._inbrengmethode.set_waarde(value, owner=self)

    @property
    def isSlotAanwezig(self) -> bool:
        """Geeft aan of er al dan niet een slot aanwezig is."""
        return self._isSlotAanwezig.get_waarde()

    @isSlotAanwezig.setter
    def isSlotAanwezig(self, value):
        self._isSlotAanwezig.set_waarde(value, owner=self)
