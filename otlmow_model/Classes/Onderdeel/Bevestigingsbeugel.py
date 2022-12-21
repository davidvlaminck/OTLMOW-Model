# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.BevestigingGC import BevestigingGC
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlBevestigingsbeugelType import KlBevestigingsbeugelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestigingsbeugel(BevestigingGC, AIMNaamObject):
    """Verbindingsstuk waarmee een object kan vastgemaakt worden aan een steun of oppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        BevestigingGC.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OmegaElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast')

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

        self._type = OTLAttribuut(field=KlBevestigingsbeugelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel.type',
                                  definition='Het type van de bevestigingsbeugel.',
                                  owner=self)

    @property
    def berekeningsnota(self) -> List[DtcDocumentWaarden]:
        """Document met de berekeningsnota van de bevestigingsbeugel."""
        return self._berekeningsnota.get_waarde()

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def constructieEnMontageplan(self) -> List[DtcDocumentWaarden]:
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
    def type(self) -> str:
        """Het type van de bevestigingsbeugel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
