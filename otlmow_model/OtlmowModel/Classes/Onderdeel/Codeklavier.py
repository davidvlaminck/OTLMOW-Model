# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlCodeklavierMerk import KlCodeklavierMerk
from ...Datatypes.KlCodeklavierModelnaam import KlCodeklavierModelnaam
from ...Datatypes.KlCodeklavierWerking import KlCodeklavierWerking
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Codeklavier(AIMNaamObject, PuntGeometrie):
    """Toestel voor het aansturen van een asset op basis van ingetoetste codes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlCodeklavierMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.merk',
                                  definition='Het merk van het codeklavier.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCodeklavierModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.modelnaam',
                                       definition='De modelnaam van het codeklavier.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.technischeFiche',
                                             definition='De technische fiche van het codeklavier.',
                                             owner=self)

        self._werking = OTLAttribuut(field=KlCodeklavierWerking,
                                     naam='werking',
                                     label='werking',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier.werking',
                                     definition='Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet.',
                                     owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het codeklavier."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het codeklavier."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het codeklavier."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def werking(self) -> str:
        """Indeling van het toestel volgens de manier waarop de gebruiker de aansturing doet."""
        return self._werking.get_waarde()

    @werking.setter
    def werking(self, value):
        self._werking.set_waarde(value, owner=self)
