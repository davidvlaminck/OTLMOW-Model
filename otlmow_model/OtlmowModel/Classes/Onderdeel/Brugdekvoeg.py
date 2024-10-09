# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlTypeBrugdekvoeg import KlTypeBrugdekvoeg
from ...Datatypes.KlTypeVerankeringBrugdekvoeg import KlTypeVerankeringBrugdekvoeg
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugdekvoeg(AIMNaamObject, LijnGeometrie):
    """Voegconstructie die dient om een opening te overbruggen. Voldoende vervormbaar om zich te kunnen aanpassen aan de bewegingen van de boorden en weerstandbiedend om belastingen te kunnen opvangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='u')  # u = unidirectional

        self._beschikbareVoegopening = OTLAttribuut(field=KwantWrdInCentimeter,
                                                    naam='beschikbareVoegopening',
                                                    label='beschikbare voegopening',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.beschikbareVoegopening',
                                                    definition='De beschikbare voegopening van de brugdekvoeg bij een gemiddelde temperatuur van 10 °C, uitgedrukt in centimeter.',
                                                    owner=self)

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.detailplan',
                                        definition='Het detailplan van de brugdekvoeg.',
                                        owner=self)

        self._heeftGeluidsreducerendElementen = OTLAttribuut(field=BooleanField,
                                                             naam='heeftGeluidsreducerendElementen',
                                                             label='heeft geluidsreducerend elementen',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.heeftGeluidsreducerendElementen',
                                                             definition='Geeft aan of de brugdekvoeg, al dan niet, geluidsreducerend elementen heeft.',
                                                             owner=self)

        self._lopendeMeterVoeg = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='lopendeMeterVoeg',
                                              label='lopende meter voeg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.lopendeMeterVoeg',
                                              definition='De lopende meter van de brugdekvoeg.',
                                              owner=self)

        self._producent = OTLAttribuut(field=StringField,
                                       naam='producent',
                                       label='producent',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.producent',
                                       definition='De producent die de brugdekvoeg heeft gemaakt.',
                                       owner=self)

        self._typeBrugdekvoeg = OTLAttribuut(field=KlTypeBrugdekvoeg,
                                             naam='typeBrugdekvoeg',
                                             label='type brugdekvoeg',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.typeBrugdekvoeg',
                                             definition='Het type van de brugdekvoeg.',
                                             owner=self)

        self._typeVerankering = OTLAttribuut(field=KlTypeVerankeringBrugdekvoeg,
                                             naam='typeVerankering',
                                             label='type verankering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.typeVerankering',
                                             definition='Het type van de verankering van de brugdekvoeg.',
                                             owner=self)

    @property
    def beschikbareVoegopening(self) -> KwantWrdInCentimeterWaarden:
        """De beschikbare voegopening van de brugdekvoeg bij een gemiddelde temperatuur van 10 °C, uitgedrukt in centimeter."""
        return self._beschikbareVoegopening.get_waarde()

    @beschikbareVoegopening.setter
    def beschikbareVoegopening(self, value):
        self._beschikbareVoegopening.set_waarde(value, owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Het detailplan van de brugdekvoeg."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def heeftGeluidsreducerendElementen(self) -> bool:
        """Geeft aan of de brugdekvoeg, al dan niet, geluidsreducerend elementen heeft."""
        return self._heeftGeluidsreducerendElementen.get_waarde()

    @heeftGeluidsreducerendElementen.setter
    def heeftGeluidsreducerendElementen(self, value):
        self._heeftGeluidsreducerendElementen.set_waarde(value, owner=self)

    @property
    def lopendeMeterVoeg(self) -> KwantWrdInMeterWaarden:
        """De lopende meter van de brugdekvoeg."""
        return self._lopendeMeterVoeg.get_waarde()

    @lopendeMeterVoeg.setter
    def lopendeMeterVoeg(self, value):
        self._lopendeMeterVoeg.set_waarde(value, owner=self)

    @property
    def producent(self) -> str:
        """De producent die de brugdekvoeg heeft gemaakt."""
        return self._producent.get_waarde()

    @producent.setter
    def producent(self, value):
        self._producent.set_waarde(value, owner=self)

    @property
    def typeBrugdekvoeg(self) -> str:
        """Het type van de brugdekvoeg."""
        return self._typeBrugdekvoeg.get_waarde()

    @typeBrugdekvoeg.setter
    def typeBrugdekvoeg(self, value):
        self._typeBrugdekvoeg.set_waarde(value, owner=self)

    @property
    def typeVerankering(self) -> str:
        """Het type van de verankering van de brugdekvoeg."""
        return self._typeVerankering.get_waarde()

    @typeVerankering.setter
    def typeVerankering(self, value):
        self._typeVerankering.set_waarde(value, owner=self)
