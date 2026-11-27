# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Lichtmast import Lichtmast
from ...Datatypes.DtuWvLichtmastBevsToestelMethode import (
    DtuWvLichtmastBevsToestelMethode,
    DtuWvLichtmastBevsToestelMethodeWaarden,
)
from ...Datatypes.KlWvLichtmastAantArmen import KlWvLichtmastAantArmen
from ...Datatypes.KlWvLichtmastArmlengte import KlWvLichtmastArmlengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVLichtmast(Lichtmast):
    """Paal voorzien van armen voor het bevestigen van wegverlichtingstoestellen. Omvat het deurtje, klemmenblok, de bevestigingsmaterialen (bv. voetplaten) en fundering of verankeringsmassief. Gebruik Lichtmast voor de bevestiging van andere toestellen dan wegverlichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalArmen = OTLAttribuut(field=KlWvLichtmastAantArmen,
                                         naam='aantalArmen',
                                         label='aantal armen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen',
                                         definition='Aantal armen van de lichtmast.',
                                         owner=self)

        self._armlengte = OTLAttribuut(field=KlWvLichtmastArmlengte,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.armlengte',
                                       definition='Lengte van de arm van de lichtmast in meter.',
                                       owner=self)

        self._bevestigingToestellen = OTLAttribuut(field=DtuWvLichtmastBevsToestelMethode,
                                                   naam='bevestigingToestellen',
                                                   label='bevestiging toestellen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.bevestigingToestellen',
                                                   kardinaliteit_max='*',
                                                   definition='Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt.',
                                                   owner=self)

    @property
    def aantalArmen(self) -> str:
        """Aantal armen van de lichtmast."""
        return self._aantalArmen.get_waarde()

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def armlengte(self) -> str:
        """Lengte van de arm van de lichtmast in meter."""
        return self._armlengte.get_waarde()

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def bevestigingToestellen(self) -> list[DtuWvLichtmastBevsToestelMethodeWaarden]:
        """Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."""
        return self._bevestigingToestellen.get_waarde()

    @bevestigingToestellen.setter
    def bevestigingToestellen(self, value):
        self._bevestigingToestellen.set_waarde(value, owner=self)
