# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlSmeringType import KlSmeringType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidingsmechanisme(TechnischDocument, PuntGeometrie):
    """Abstracte om relaties en attributen te bundelen voor geleidingsmechanismen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleidingsmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._aantalSmeerpunten = OTLAttribuut(field=IntegerField,
                                               naam='aantalSmeerpunten',
                                               label='aantal smeerpunten',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleidingsmechanisme.aantalSmeerpunten',
                                               definition='Het aantal smeerpunten.',
                                               owner=self)

        self._typeSmering = OTLAttribuut(field=KlSmeringType,
                                         naam='typeSmering',
                                         label='type smering',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geleidingsmechanisme.typeSmering',
                                         definition='Geeft aan op welke wijze het lager gesmeerd wordt.',
                                         owner=self)

    @property
    def aantalSmeerpunten(self) -> int:
        """Het aantal smeerpunten."""
        return self._aantalSmeerpunten.get_waarde()

    @aantalSmeerpunten.setter
    def aantalSmeerpunten(self, value):
        self._aantalSmeerpunten.set_waarde(value, owner=self)

    @property
    def typeSmering(self) -> str:
        """Geeft aan op welke wijze het lager gesmeerd wordt."""
        return self._typeSmering.get_waarde()

    @typeSmering.setter
    def typeSmering(self, value):
        self._typeSmering.set_waarde(value, owner=self)
