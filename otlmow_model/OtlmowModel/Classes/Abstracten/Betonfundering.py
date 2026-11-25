# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Fundering import Fundering
from ...Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM, DtcAfmetingBxlInMWaarden
from ...Datatypes.KlFunderingBetonkwaliteit import KlFunderingBetonkwaliteit
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonfundering(Fundering, VlakGeometrie):
    """Abstracte voor funderingen in beton."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'u', '2.0.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', '2.0.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', '2.0.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', '2.0.0'),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInM,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.afmetingGrondvlak',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                               deprecated_version='2.0.0',
                                               definition='De maximale lengte en breedte van bovenkant van de fundering.',
                                               owner=self)

        self._betonkwaliteit = OTLAttribuut(field=KlFunderingBetonkwaliteit,
                                            naam='betonkwaliteit',
                                            label='betonkwaliteit',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.betonkwaliteit',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden.',
                                            owner=self)

    @property
    def afmetingGrondvlak(self) -> DtcAfmetingBxlInMWaarden:
        """De maximale lengte en breedte van bovenkant van de fundering."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def betonkwaliteit(self) -> str:
        """Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden."""
        return self._betonkwaliteit.get_waarde()

    @betonkwaliteit.setter
    def betonkwaliteit(self, value):
        self._betonkwaliteit.set_waarde(value, owner=self)
