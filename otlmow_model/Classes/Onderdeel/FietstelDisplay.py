# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class FietstelDisplay(AIMNaamObject, PuntGeometrie, VlakGeometrie):
    """Verankerd toestel dat een selectie van telgegevens van het fietstelsysteem toont voor passerende fietsers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fietstelinstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem')

        self._isDubbelzijdig = OTLAttribuut(field=BooleanField,
                                            naam='isDubbelzijdig',
                                            label='is dubbelzijdig',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.isDubbelzijdig',
                                            definition='Geeft aan of het display telgegevens toont langs zijn beide zijden of niet.',
                                            owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.technischeFiche',
                                             definition='Document met de technische specificaties van het display.',
                                             owner=self)

    @property
    def isDubbelzijdig(self) -> bool:
        """Geeft aan of het display telgegevens toont langs zijn beide zijden of niet."""
        return self._isDubbelzijdig.get_waarde()

    @isDubbelzijdig.setter
    def isDubbelzijdig(self, value):
        self._isDubbelzijdig.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document met de technische specificaties van het display."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
