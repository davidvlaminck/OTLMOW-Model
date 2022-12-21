# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlTypeBrugligger import KlTypeBrugligger
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugligger(ConstructiefObject, LijnGeometrie):
    """Ondersteunende balkstructuur van een brug onder het brugdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        ConstructiefObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')

        self._detailplanBrugligger = OTLAttribuut(field=DtcDocument,
                                                  naam='detailplanBrugligger',
                                                  label='detailplan brugligger',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger.detailplanBrugligger',
                                                  definition='Tekening of plan van de brugligger. Deze omvat o.a. ook afmetingen,...',
                                                  owner=self)

        self._type = OTLAttribuut(field=KlTypeBrugligger,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger.type',
                                  definition='Het type van brugligger.',
                                  owner=self)

    @property
    def detailplanBrugligger(self) -> DtcDocumentWaarden:
        """Tekening of plan van de brugligger. Deze omvat o.a. ook afmetingen,..."""
        return self._detailplanBrugligger.get_waarde()

    @detailplanBrugligger.setter
    def detailplanBrugligger(self, value):
        self._detailplanBrugligger.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van brugligger."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
