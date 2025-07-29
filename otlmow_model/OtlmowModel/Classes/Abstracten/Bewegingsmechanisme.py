# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlSmeringType import KlSmeringType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bewegingsmechanisme(TechnischDocument, PuntGeometrie):
    """Abstracte om relaties en attributen te bundelen voor bewegingsmechanismen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bewegingsmechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._aantalSmeerpunten = OTLAttribuut(field=IntegerField,
                                               naam='aantalSmeerpunten',
                                               label='aantal smeerpunten',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bewegingsmechanisme.aantalSmeerpunten',
                                               definition='Het aantal aanwezige smeerpunten.',
                                               owner=self)

        self._typeSmering = OTLAttribuut(field=KlSmeringType,
                                         naam='typeSmering',
                                         label='type smering',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bewegingsmechanisme.typeSmering',
                                         definition='Geeft aan op welke wijze het lager gesmeerd wordt.',
                                         owner=self)

    @property
    def aantalSmeerpunten(self) -> int:
        """Het aantal aanwezige smeerpunten."""
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
