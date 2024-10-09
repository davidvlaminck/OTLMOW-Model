# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Baanlichaam(AIMObject, VlakGeometrie):
    """De lagen tussen het baanbed en het baanoppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.11.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u', deprecated='2.11.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='u', deprecated='2.11.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Signalisatie', direction='u', deprecated='2.11.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i', deprecated='2.11.0')  # i = direction: incoming

        self._dwarsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='dwarsprofiel',
                                          label='dwarsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.dwarsprofiel',
                                          usagenote='Klasse uit gebruik sinds versie 2.11.0 ',
                                          deprecated_version='2.11.0',
                                          definition='Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan.',
                                          owner=self)

        self._horizontaleLigging = OTLAttribuut(field=DtcDocument,
                                                naam='horizontaleLigging',
                                                label='horizontale ligging',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.horizontaleLigging',
                                                usagenote='Klasse uit gebruik sinds versie 2.11.0 ',
                                                deprecated_version='2.11.0',
                                                definition='De horizontale ligging van het baanlichaam als document bijlage.',
                                                owner=self)

        self._langsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='langsprofiel',
                                          label='langsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.langsprofiel',
                                          usagenote='Klasse uit gebruik sinds versie 2.11.0 ',
                                          deprecated_version='2.11.0',
                                          definition='Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan.',
                                          owner=self)

    @property
    def dwarsprofiel(self) -> DtcDocumentWaarden:
        """Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan."""
        return self._dwarsprofiel.get_waarde()

    @dwarsprofiel.setter
    def dwarsprofiel(self, value):
        self._dwarsprofiel.set_waarde(value, owner=self)

    @property
    def horizontaleLigging(self) -> DtcDocumentWaarden:
        """De horizontale ligging van het baanlichaam als document bijlage."""
        return self._horizontaleLigging.get_waarde()

    @horizontaleLigging.setter
    def horizontaleLigging(self, value):
        self._horizontaleLigging.set_waarde(value, owner=self)

    @property
    def langsprofiel(self) -> DtcDocumentWaarden:
        """Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan."""
        return self._langsprofiel.get_waarde()

    @langsprofiel.setter
    def langsprofiel(self, value):
        self._langsprofiel.set_waarde(value, owner=self)
