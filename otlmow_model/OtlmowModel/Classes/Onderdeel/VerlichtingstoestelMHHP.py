# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Verlichtingstoestel import Verlichtingstoestel
from ...Classes.Abstracten.VerlichtingstoestelConnector import (
    VerlichtingstoestelConnector,
)
from ...Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelMHHP(Verlichtingstoestel, VerlichtingstoestelConnector):
    """Het geheel van de metaalhalogenide lamp (MHHP), voorschakelapparatuur en de behuizing die werden samengesteld met als doel: * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen; * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt; * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.armatuurkleur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?',
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
