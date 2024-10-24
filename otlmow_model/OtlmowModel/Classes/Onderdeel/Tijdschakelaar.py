# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlTijdschakelaarUitvoering import KlTijdschakelaarUitvoering
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tijdschakelaar(AIMNaamObject, PuntGeometrie):
    """Een apparaat met een interne klok dat een stuursignaal uitstuurt nadat de klok een specifiek tijdsinterval heeft opgemeten. Ook klokschakelaar of timer genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tijdschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BiFlashInstallatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BiFlash', direction='o')  # o = direction: outgoing

        self._componentnummer = OTLAttribuut(field=StringField,
                                             naam='componentnummer',
                                             label='componentnummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tijdschakelaar.componentnummer',
                                             definition='Het componentnummer van het elektrische toestel, zoals weergegeven op het schema van het lokale laagspanningsbord. Wordt ook wel onderdeelcode (ODC) genoemd.',
                                             owner=self)

        self._instellingen = OTLAttribuut(field=DtcDocument,
                                          naam='instellingen',
                                          label='instellingen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tijdschakelaar.instellingen',
                                          definition='Het tijdsschema voor schakelingen als tekst.',
                                          owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tijdschakelaar.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

        self._uitvoering = OTLAttribuut(field=KlTijdschakelaarUitvoering,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tijdschakelaar.uitvoering',
                                        definition='Indeling van de tijdschakelaar volgens de manier waarop instellingen ingegeven worden.',
                                        owner=self)

    @property
    def componentnummer(self) -> str:
        """Het componentnummer van het elektrische toestel, zoals weergegeven op het schema van het lokale laagspanningsbord. Wordt ook wel onderdeelcode (ODC) genoemd."""
        return self._componentnummer.get_waarde()

    @componentnummer.setter
    def componentnummer(self, value):
        self._componentnummer.set_waarde(value, owner=self)

    @property
    def instellingen(self) -> DtcDocumentWaarden:
        """Het tijdsschema voor schakelingen als tekst."""
        return self._instellingen.get_waarde()

    @instellingen.setter
    def instellingen(self, value):
        self._instellingen.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """Indeling van de tijdschakelaar volgens de manier waarop instellingen ingegeven worden."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
