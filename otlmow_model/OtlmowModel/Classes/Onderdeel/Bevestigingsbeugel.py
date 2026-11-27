# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BevestigingGC import BevestigingGC
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBevestigingsbeugelType import KlBevestigingsbeugelType
from ...Datatypes.KlMateriaalBevestigingsbeugel import KlMateriaalBevestigingsbeugel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestigingsbeugel(BevestigingGC, AIMNaamObject):
    """Verbindingsstuk waarmee een object kan vastgemaakt worden aan een steun of oppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BVAfwateringKunstwerken', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koppelbalk', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Illuminator', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetbocht', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._berekeningsnota = OTLAttribuut(field=DtcDocument,
                                             naam='berekeningsnota',
                                             label='berekeningsnota',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.berekeningsnota',
                                             usagenote='Bestanden van het type xlsx of pdf.',
                                             kardinaliteit_max='*',
                                             definition='Document met de berekeningsnota van de bevestigingsbeugel.',
                                             owner=self)

        self._constructieEnMontageplan = OTLAttribuut(field=DtcDocument,
                                                      naam='constructieEnMontageplan',
                                                      label='constructie en montageplan',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.constructieEnMontageplan',
                                                      usagenote='Bestanden van het type dwg of pdf.',
                                                      kardinaliteit_max='*',
                                                      definition='Document met het constructie- en montageplan van de bevestigingsbeugel.',
                                                      owner=self)

        self._heeftVeiligheidsstrip = OTLAttribuut(field=BooleanField,
                                                   naam='heeftVeiligheidsstrip',
                                                   label='heeft veiligheidsstrip',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.heeftVeiligheidsstrip',
                                                   definition='Metalen strip in de beugel, die verhinderd dat het bevestigd onderdeel naar beneden zou komen (bijvoorbeeld bij brand).',
                                                   owner=self)

        self._isVerzegeld = OTLAttribuut(field=BooleanField,
                                         naam='isVerzegeld',
                                         label='is verzegeld',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.isVerzegeld',
                                         definition='Geeft aan of de bevestigingsbeugel verzegeld is tegen het ongemerkt losmaken ervan.',
                                         owner=self)

        self._materiaalBevestigingsbeugel = OTLAttribuut(field=KlMateriaalBevestigingsbeugel,
                                                         naam='materiaalBevestigingsbeugel',
                                                         label='materiaal bevestigingsbeugel',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.materiaalBevestigingsbeugel',
                                                         definition='Het materiaal waaruit de bevestigingsbeugel bestaat.',
                                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de bevestigingsbeugel.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlBevestigingsbeugelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.type',
                                  definition='Het type van de bevestigingsbeugel.',
                                  owner=self)

    @property
    def berekeningsnota(self) -> list[DtcDocumentWaarden]:
        """Document met de berekeningsnota van de bevestigingsbeugel."""
        return self._berekeningsnota.get_waarde()

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def constructieEnMontageplan(self) -> list[DtcDocumentWaarden]:
        """Document met het constructie- en montageplan van de bevestigingsbeugel."""
        return self._constructieEnMontageplan.get_waarde()

    @constructieEnMontageplan.setter
    def constructieEnMontageplan(self, value):
        self._constructieEnMontageplan.set_waarde(value, owner=self)

    @property
    def heeftVeiligheidsstrip(self) -> bool:
        """Metalen strip in de beugel, die verhinderd dat het bevestigd onderdeel naar beneden zou komen (bijvoorbeeld bij brand)."""
        return self._heeftVeiligheidsstrip.get_waarde()

    @heeftVeiligheidsstrip.setter
    def heeftVeiligheidsstrip(self, value):
        self._heeftVeiligheidsstrip.set_waarde(value, owner=self)

    @property
    def isVerzegeld(self) -> bool:
        """Geeft aan of de bevestigingsbeugel verzegeld is tegen het ongemerkt losmaken ervan."""
        return self._isVerzegeld.get_waarde()

    @isVerzegeld.setter
    def isVerzegeld(self, value):
        self._isVerzegeld.set_waarde(value, owner=self)

    @property
    def materiaalBevestigingsbeugel(self) -> str:
        """Het materiaal waaruit de bevestigingsbeugel bestaat."""
        return self._materiaalBevestigingsbeugel.get_waarde()

    @materiaalBevestigingsbeugel.setter
    def materiaalBevestigingsbeugel(self, value):
        self._materiaalBevestigingsbeugel.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> list[DtcDocumentWaarden]:
        """De technische fiche van de bevestigingsbeugel."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van de bevestigingsbeugel."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
