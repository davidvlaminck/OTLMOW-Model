# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlGewaarborgdeWrijvingshoek import KlGewaarborgdeWrijvingshoek
from otlmow_model.Datatypes.KlGrondherkomst import KlGrondherkomst
from otlmow_model.Datatypes.KlOphogingSoorten import KlOphogingSoorten
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ophoging(AIMObject):
    """Wordt beschouwd als de verzameling van beheeractiviteiten die uitgevoerd kunnen worden op grond."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging.gewicht',
                                     definition='Het gewicht van de grondlaag in ton.',
                                     owner=self)

        self._herkomst = OTLAttribuut(field=KlGrondherkomst,
                                      naam='herkomst',
                                      label='herkomst',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging.herkomst',
                                      definition='De herkomst van de grond.',
                                      owner=self)

        self._soortOphoging = OTLAttribuut(field=KlOphogingSoorten,
                                           naam='soortOphoging',
                                           label='soort ophoging',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging.soortOphoging',
                                           definition='De specificatie van type grond bij ophoging.',
                                           owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging.volume',
                                    definition='Het volume van de grondlaag in kubieke meter.',
                                    owner=self)

        self._wrijvingshoek = OTLAttribuut(field=KlGewaarborgdeWrijvingshoek,
                                           naam='wrijvingshoek',
                                           label='wrijvingshoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#Ophoging.wrijvingshoek',
                                           definition='De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen.',
                                           owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de grondlaag in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def herkomst(self) -> str:
        """De herkomst van de grond."""
        return self._herkomst.get_waarde()

    @herkomst.setter
    def herkomst(self, value):
        self._herkomst.set_waarde(value, owner=self)

    @property
    def soortOphoging(self) -> str:
        """De specificatie van type grond bij ophoging."""
        return self._soortOphoging.get_waarde()

    @soortOphoging.setter
    def soortOphoging(self, value):
        self._soortOphoging.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van de grondlaag in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)

    @property
    def wrijvingshoek(self) -> str:
        """De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen."""
        return self._wrijvingshoek.get_waarde()

    @wrijvingshoek.setter
    def wrijvingshoek(self, value):
        self._wrijvingshoek.set_waarde(value, owner=self)
