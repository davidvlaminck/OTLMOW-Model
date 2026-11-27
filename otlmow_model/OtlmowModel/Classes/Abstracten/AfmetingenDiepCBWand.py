# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Fundering import Fundering
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.Abstracten.Waterremmend import Waterremmend
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import (
    KwantWrdInMeterTAW,
    KwantWrdInMeterTAWWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfmetingenDiepCBWand(Fundering, Grondkeringen, Waterremmend, LijnGeometrie):
    """Abstracte voor het bundelen van de afmetingen van de diep- en de cement-bentonietwand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand'
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
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Funderingswand', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afkappeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                       naam='afkappeil',
                                       label='afkappeil',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand.afkappeil',
                                       definition='Het afkappeil van de wanden in mTaw.',
                                       owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand.dikte',
                                   definition='De dikte van de wand in meter',
                                   owner=self)

        self._paneelbreedte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='paneelbreedte',
                                           label='paneelbreedte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand.paneelbreedte',
                                           definition='Breedte van de wand in meter.',
                                           owner=self)

        self._totaleHorizontaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                                     naam='totaleHorizontaleLengte',
                                                     label='totale horizontale lengte',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand.totaleHorizontaleLengte',
                                                     definition='De totale horizontale lengte van de wand in lopende meter.',
                                                     owner=self)

    @property
    def afkappeil(self) -> KwantWrdInMeterTAWWaarden:
        """Het afkappeil van de wanden in mTaw."""
        return self._afkappeil.get_waarde()

    @afkappeil.setter
    def afkappeil(self, value):
        self._afkappeil.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMeterWaarden:
        """De dikte van de wand in meter"""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def paneelbreedte(self) -> KwantWrdInMeterWaarden:
        """Breedte van de wand in meter."""
        return self._paneelbreedte.get_waarde()

    @paneelbreedte.setter
    def paneelbreedte(self, value):
        self._paneelbreedte.set_waarde(value, owner=self)

    @property
    def totaleHorizontaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale horizontale lengte van de wand in lopende meter."""
        return self._totaleHorizontaleLengte.get_waarde()

    @totaleHorizontaleLengte.setter
    def totaleHorizontaleLengte(self, value):
        self._totaleHorizontaleLengte.set_waarde(value, owner=self)
