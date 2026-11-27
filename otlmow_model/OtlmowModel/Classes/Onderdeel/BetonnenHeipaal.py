# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from ...Datatypes.KlTypeSchachtHeipaal import KlTypeSchachtHeipaal
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenHeipaal(BetonnenConstructieElement, Funderingspaal):
    """Betonnen paal die in de grond wordt gebracht door deze in een hei-installatie te plaatsen waarna men er een zwaar gewicht (heiblok) op laat vallen. De grond onder de paal wordt samengeperst waardoor de draagkracht groter wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal'
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
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameterPaalschacht = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='diameterPaalschacht',
                                                 label='diameter paalschacht',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.diameterPaalschacht',
                                                 definition='Doorsnede in millimeter van de schacht van de paal.',
                                                 owner=self)

        self._heeftVerbredeVoet = OTLAttribuut(field=BooleanField,
                                               naam='heeftVerbredeVoet',
                                               label='heeft verbrede voet',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerbredeVoet',
                                               definition='Geeft aan of de voet breder is gemaakt, al dan niet.',
                                               owner=self)

        self._heeftVerlorenVoerbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftVerlorenVoerbuis',
                                                   label='heeft verloren voerbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.heeftVerlorenVoerbuis',
                                                   definition='Aanduiding of de heipaal een verloren voerbuis heeft.',
                                                   owner=self)

        self._nuttigeLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='nuttigeLengte',
                                           label='nuttige lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.nuttigeLengte',
                                           definition='Afstand gemeten, in meter, volgens de as van de heipaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het bovenpeil) en het aanzetpeil (definitief funderingspeil).',
                                           owner=self)

        self._typeSchacht = OTLAttribuut(field=KlTypeSchachtHeipaal,
                                         naam='typeSchacht',
                                         label='type schacht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenHeipaal.typeSchacht',
                                         definition='De soort schacht van de heipaal.',
                                         owner=self)

    @property
    def diameterPaalschacht(self) -> KwantWrdInMillimeterWaarden:
        """Doorsnede in millimeter van de schacht van de paal."""
        return self._diameterPaalschacht.get_waarde()

    @diameterPaalschacht.setter
    def diameterPaalschacht(self, value):
        self._diameterPaalschacht.set_waarde(value, owner=self)

    @property
    def heeftVerbredeVoet(self) -> bool:
        """Geeft aan of de voet breder is gemaakt, al dan niet."""
        return self._heeftVerbredeVoet.get_waarde()

    @heeftVerbredeVoet.setter
    def heeftVerbredeVoet(self, value):
        self._heeftVerbredeVoet.set_waarde(value, owner=self)

    @property
    def heeftVerlorenVoerbuis(self) -> bool:
        """Aanduiding of de heipaal een verloren voerbuis heeft."""
        return self._heeftVerlorenVoerbuis.get_waarde()

    @heeftVerlorenVoerbuis.setter
    def heeftVerlorenVoerbuis(self, value):
        self._heeftVerlorenVoerbuis.set_waarde(value, owner=self)

    @property
    def nuttigeLengte(self) -> KwantWrdInMeterWaarden:
        """Afstand gemeten, in meter, volgens de as van de heipaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het bovenpeil) en het aanzetpeil (definitief funderingspeil)."""
        return self._nuttigeLengte.get_waarde()

    @nuttigeLengte.setter
    def nuttigeLengte(self, value):
        self._nuttigeLengte.set_waarde(value, owner=self)

    @property
    def typeSchacht(self) -> str:
        """De soort schacht van de heipaal."""
        return self._typeSchacht.get_waarde()

    @typeSchacht.setter
    def typeSchacht(self, value):
        self._typeSchacht.set_waarde(value, owner=self)
