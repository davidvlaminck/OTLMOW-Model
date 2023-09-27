# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Verlichtingstoestel import Verlichtingstoestel
from otlmow_model.Classes.Abstracten.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden
from otlmow_model.Datatypes.KlArmatuurkleur import KlArmatuurkleur


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelNaHP(Verlichtingstoestel, VerlichtingstoestelConnector):
    """Het geheel van de natrium hoge druk lamp (NaHP) en de behuizing die werden samengesteld met als doel: * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen; * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt; * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat')

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.armatuurkleur',
                                           usagenote='Attribuut uit gebruik sinds versie 2.3.0 ',
                                           deprecated_version='2.3.0',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti-vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?',
                                                 owner=self)

        self._heeftSperfilter = OTLAttribuut(field=BooleanField,
                                             naam='heeftSperfilter',
                                             label='heeft sperfilter',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftSperfilter',
                                             definition='Is er een sperfilter aanwezig?',
                                             owner=self)

        self._kleurArmatuur = OTLAttribuut(field=KlArmatuurkleur,
                                           naam='kleurArmatuur',
                                           label='kleur armatuur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.kleurArmatuur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

    @property
    def armatuurkleur(self) -> DteKleurRALWaarden:
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        return self._armatuurkleur.get_waarde()

    @armatuurkleur.setter
    def armatuurkleur(self, value):
        self._armatuurkleur.set_waarde(value, owner=self)

    @property
    def heeftAntiVandalisme(self) -> bool:
        """Is het een antivandalisme type verlichtingstoestel?"""
        return self._heeftAntiVandalisme.get_waarde()

    @heeftAntiVandalisme.setter
    def heeftAntiVandalisme(self, value):
        self._heeftAntiVandalisme.set_waarde(value, owner=self)

    @property
    def heeftSperfilter(self) -> bool:
        """Is er een sperfilter aanwezig?"""
        return self._heeftSperfilter.get_waarde()

    @heeftSperfilter.setter
    def heeftSperfilter(self, value):
        self._heeftSperfilter.set_waarde(value, owner=self)

    @property
    def kleurArmatuur(self) -> str:
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        return self._kleurArmatuur.get_waarde()

    @kleurArmatuur.setter
    def kleurArmatuur(self, value):
        self._kleurArmatuur.set_waarde(value, owner=self)
