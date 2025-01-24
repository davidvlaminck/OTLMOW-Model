# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondanker import Grondanker
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenTrekstaaf(Grondanker, AIMNaamObject):
    """Verbindingselement tussen 2 wanden, bv. ronde staven. Toegepast bij (passieve) ankerschotten, kofferdammen,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional

        self._dienstlast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                        naam='dienstlast',
                                        label='dienstlast',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.dienstlast',
                                        definition='De trekkracht (karakteristieke waarde) die de stalen trekstaaf moet opnemen.',
                                        owner=self)

        self._heeftHDPEBuis = OTLAttribuut(field=BooleanField,
                                           naam='heeftHDPEBuis',
                                           label='heeft HDPE buis',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.heeftHDPEBuis',
                                           definition='Geeft aan of een HDPE buis gebruikt wordt in de uitvoering.',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.lengte',
                                    definition='Lengte van de stalentrekstaaf in centimeter',
                                    owner=self)

        self._peilAnkerkop = OTLAttribuut(field=KwantWrdInMeterTAW,
                                          naam='peilAnkerkop',
                                          label='peil ankerkop',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.peilAnkerkop',
                                          definition='Het peil van de kop van het anker',
                                          owner=self)

        self._peilAnkerwand = OTLAttribuut(field=KwantWrdInMeterTAW,
                                           naam='peilAnkerwand',
                                           label='peil ankerwand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.peilAnkerwand',
                                           definition='Het peil van het anker in de wand',
                                           owner=self)

        self._voorspankracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                            naam='voorspankracht',
                                            label='voorspankracht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenTrekstaaf.voorspankracht',
                                            definition='Kracht waarbij het anker vastgezet wordt door de opdrachtnemer na aftrek van de te verwachten spanningsverliezen in hetanker.',
                                            owner=self)

    @property
    def dienstlast(self) -> KwantWrdInKiloNewtonWaarden:
        """De trekkracht (karakteristieke waarde) die de stalen trekstaaf moet opnemen."""
        return self._dienstlast.get_waarde()

    @dienstlast.setter
    def dienstlast(self, value):
        self._dienstlast.set_waarde(value, owner=self)

    @property
    def heeftHDPEBuis(self) -> bool:
        """Geeft aan of een HDPE buis gebruikt wordt in de uitvoering."""
        return self._heeftHDPEBuis.get_waarde()

    @heeftHDPEBuis.setter
    def heeftHDPEBuis(self, value):
        self._heeftHDPEBuis.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInCentimeterWaarden:
        """Lengte van de stalentrekstaaf in centimeter"""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def peilAnkerkop(self) -> KwantWrdInMeterTAWWaarden:
        """Het peil van de kop van het anker"""
        return self._peilAnkerkop.get_waarde()

    @peilAnkerkop.setter
    def peilAnkerkop(self, value):
        self._peilAnkerkop.set_waarde(value, owner=self)

    @property
    def peilAnkerwand(self) -> KwantWrdInMeterTAWWaarden:
        """Het peil van het anker in de wand"""
        return self._peilAnkerwand.get_waarde()

    @peilAnkerwand.setter
    def peilAnkerwand(self, value):
        self._peilAnkerwand.set_waarde(value, owner=self)

    @property
    def voorspankracht(self) -> KwantWrdInKiloNewtonWaarden:
        """Kracht waarbij het anker vastgezet wordt door de opdrachtnemer na aftrek van de te verwachten spanningsverliezen in hetanker."""
        return self._voorspankracht.get_waarde()

    @voorspankracht.setter
    def voorspankracht(self, value):
        self._voorspankracht.set_waarde(value, owner=self)
