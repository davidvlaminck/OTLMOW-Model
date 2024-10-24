# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlStopcontactAantalPolen import KlStopcontactAantalPolen
from ...Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from ...Datatypes.KwantWrdInVolt import KwantWrdInVolt, KwantWrdInVoltWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stopcontact(AIMObject, PuntGeometrie):
    """Een aansluitpunt op het elektrisch net voor afname van elektrische energie met behulp van een stekker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._aantalPolen = OTLAttribuut(field=KlStopcontactAantalPolen,
                                         naam='aantalPolen',
                                         label='aantal polen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.aantalPolen',
                                         definition='Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst.',
                                         owner=self)

        self._spanning = OTLAttribuut(field=KwantWrdInVolt,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.spanning',
                                      definition='De voorziene spanning voor het stopcontact.',
                                      owner=self)

        self._stroomsterkte = OTLAttribuut(field=KwantWrdInAmpere,
                                           naam='stroomsterkte',
                                           label='stroomsterkte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stopcontact.stroomsterkte',
                                           definition='Maximale stroomsterkte van het stopcontact uitgedrukt in ampère.',
                                           owner=self)

    @property
    def aantalPolen(self) -> str:
        """Typering van het stopcontact volgens het aantal polen op basis van een keuzelijst."""
        return self._aantalPolen.get_waarde()

    @aantalPolen.setter
    def aantalPolen(self, value):
        self._aantalPolen.set_waarde(value, owner=self)

    @property
    def spanning(self) -> KwantWrdInVoltWaarden:
        """De voorziene spanning voor het stopcontact."""
        return self._spanning.get_waarde()

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self)

    @property
    def stroomsterkte(self) -> KwantWrdInAmpereWaarden:
        """Maximale stroomsterkte van het stopcontact uitgedrukt in ampère."""
        return self._stroomsterkte.get_waarde()

    @stroomsterkte.setter
    def stroomsterkte(self, value):
        self._stroomsterkte.set_waarde(value, owner=self)
