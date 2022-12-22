# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Kast import Kast
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlLockerkastMerk import KlLockerkastMerk
from otlmow_model.Datatypes.KlLockerkastModelnaam import KlLockerkastModelnaam
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lockerkast(Kast):
    """Een lockerkast is een geheel dat onderverdeeld is in een aantal kleinere en smallere opslagruimtes, bedoeld voor het opslaan van persoonlijke goederen of bezittingen. De lockers kunnen vaak afzonderlijk geopend en afgesloten worden. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockermanagementmodule')

        self._aantalLockers = OTLAttribuut(field=NonNegIntegerField,
                                           naam='aantalLockers',
                                           label='aantal lockers',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast.aantalLockers',
                                           definition='Het aantal individuele lockers aanwezig in de lockerkast.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlLockerkastMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast.merk',
                                  definition='Het merk van de lockerkast.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLockerkastModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast.modelnaam',
                                       definition='De modelnaam van de lockerkast.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast.technischeFiche',
                                             definition='De technische fiche van de lockerkast.',
                                             owner=self)

    @property
    def aantalLockers(self) -> int:
        """Het aantal individuele lockers aanwezig in de lockerkast."""
        return self._aantalLockers.get_waarde()

    @aantalLockers.setter
    def aantalLockers(self, value):
        self._aantalLockers.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de lockerkast."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de lockerkast."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de lockerkast."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
