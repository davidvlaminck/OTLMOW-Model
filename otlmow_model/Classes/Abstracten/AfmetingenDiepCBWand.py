# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Fundering import Fundering
from otlmow_model.Classes.Abstracten.Grondkeringen import Grondkeringen
from otlmow_model.Classes.Abstracten.Waterremmend import Waterremmend
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfmetingenDiepCBWand(Fundering, Grondkeringen, Waterremmend, LijnGeometrie):
    """Abstracte voor het bundelen van de afmetingen van de diep- en de cement-bentonietwand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfmetingenDiepCBWand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Funderingswand')

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
