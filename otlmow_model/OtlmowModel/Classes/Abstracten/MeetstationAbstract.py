# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcMeteoFoto import DtcMeteoFoto, DtcMeteoFotoWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeetstationAbstract(PuntGeometrie, VlakGeometrie):
    """Bundeling van de generieke eigenschappen en relaties voor een meetstation."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt', direction='i')  # i = direction: incoming

        self._foto = OTLAttribuut(field=DtcMeteoFoto,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract.foto',
                                  kardinaliteit_max='*',
                                  definition="De verschillende foto's van het meetstation.",
                                  owner=self)

        self._heeftMaaibescherming = OTLAttribuut(field=BooleanField,
                                                  naam='heeftMaaibescherming',
                                                  label='heeft maaibescherming',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract.heeftMaaibescherming',
                                                  definition='Bepaalt of er al dan niet maaibescherming aanwezig is.',
                                                  owner=self)

        self._keuringsrapport = OTLAttribuut(field=DtcDocument,
                                             naam='keuringsrapport',
                                             label='keuringsrapport',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract.keuringsrapport',
                                             kardinaliteit_max='*',
                                             definition='Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation.',
                                             owner=self)

        self._onderhoudsrapport = OTLAttribuut(field=DtcDocument,
                                               naam='onderhoudsrapport',
                                               label='onderhoudsrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract.onderhoudsrapport',
                                               kardinaliteit_max='*',
                                               definition='Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation.',
                                               owner=self)

    @property
    def foto(self) -> List[DtcMeteoFotoWaarden]:
        """De verschillende foto's van het meetstation."""
        return self._foto.get_waarde()

    @foto.setter
    def foto(self, value):
        self._foto.set_waarde(value, owner=self)

    @property
    def heeftMaaibescherming(self) -> bool:
        """Bepaalt of er al dan niet maaibescherming aanwezig is."""
        return self._heeftMaaibescherming.get_waarde()

    @heeftMaaibescherming.setter
    def heeftMaaibescherming(self, value):
        self._heeftMaaibescherming.set_waarde(value, owner=self)

    @property
    def keuringsrapport(self) -> List[DtcDocumentWaarden]:
        """Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation."""
        return self._keuringsrapport.get_waarde()

    @keuringsrapport.setter
    def keuringsrapport(self, value):
        self._keuringsrapport.set_waarde(value, owner=self)

    @property
    def onderhoudsrapport(self) -> List[DtcDocumentWaarden]:
        """Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation."""
        return self._onderhoudsrapport.get_waarde()

    @onderhoudsrapport.setter
    def onderhoudsrapport(self, value):
        self._onderhoudsrapport.set_waarde(value, owner=self)
