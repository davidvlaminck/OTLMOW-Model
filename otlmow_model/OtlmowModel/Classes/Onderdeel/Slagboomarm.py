# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSlagboomarmMerk import KlSlagboomarmMerk
from ...Datatypes.KlSlagboomarmModelnaam import KlSlagboomarmModelnaam
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboomarm(AIMObject, LijnGeometrie):
    """De bewegende arm van een slagboominstallatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SlagboomarmVerlichting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom', direction='o')  # o = direction: outgoing

        self._lengteBoom = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='lengteBoom',
                                        label='lengte boom',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.lengteBoom',
                                        definition='De lengte van de slagboomarm uitgedrukt in meter.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlSlagboomarmMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.merk',
                                  definition='Het merk van de slagboom installatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSlagboomarmModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.modelnaam',
                                       definition='Naam van het model van de slagboominstallatie.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm.technischeFiche',
                                             definition='Technische fiche van de slagboominstallatie.',
                                             owner=self)

    @property
    def lengteBoom(self) -> KwantWrdInMeterWaarden:
        """De lengte van de slagboomarm uitgedrukt in meter."""
        return self._lengteBoom.get_waarde()

    @lengteBoom.setter
    def lengteBoom(self, value):
        self._lengteBoom.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de slagboom installatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam van het model van de slagboominstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche van de slagboominstallatie."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
