# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcMeteoFoto import DtcMeteoFoto, DtcMeteoFotoWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeetstationAbstract(PuntGeometrie, VlakGeometrie):
    """Bundeling van de generieke eigenschappen en relaties voor een meetstation."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
                                             usagenote='Attribuut uit gebruik sinds versie 2.20.0 ',
                                             deprecated_version='2.20.0',
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
    def foto(self) -> list[DtcMeteoFotoWaarden]:
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
    def keuringsrapport(self) -> list[DtcDocumentWaarden]:
        """Het rapport dat 5 jaarlijks wordt opgesteld met details over het meetstation."""
        return self._keuringsrapport.get_waarde()

    @keuringsrapport.setter
    def keuringsrapport(self, value):
        self._keuringsrapport.set_waarde(value, owner=self)

    @property
    def onderhoudsrapport(self) -> list[DtcDocumentWaarden]:
        """Het rapport dat jaarlijks wordt opgesteld met details over het onderhoud van het meetstation."""
        return self._onderhoudsrapport.get_waarde()

    @onderhoudsrapport.setter
    def onderhoudsrapport(self, value):
        self._onderhoudsrapport.set_waarde(value, owner=self)
