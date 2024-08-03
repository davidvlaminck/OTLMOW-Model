# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class OntwerpwaterstandStreefpeil(VlakGeometrie):
    """Abstracte om de streefpeilen en relevante ontwerpwaterstanden (afwaarts & opwaarts) van sluizen en stuwen te bundelen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OntwerpwaterstandStreefpeil'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._relevanteOntwerpWaterstandAfwaarts = OTLAttribuut(field=StringField,
                                                                naam='relevanteOntwerpWaterstandAfwaarts',
                                                                label='relevante ontwerpwaterstand afwaarts',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OntwerpwaterstandStreefpeil.relevanteOntwerpWaterstandAfwaarts',
                                                                definition='De relevante ontwerpwaterstand afwaarts van de waterbouwkundige constructie.',
                                                                owner=self)

        self._relevanteOntwerpWaterstandOpwaarts = OTLAttribuut(field=StringField,
                                                                naam='relevanteOntwerpWaterstandOpwaarts',
                                                                label='relevante ontwerpwaterstand opwaarts',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OntwerpwaterstandStreefpeil.relevanteOntwerpWaterstandOpwaarts',
                                                                definition='De relevante ontwerpwaterstand opwaarts van de waterbouwkundige constructie.',
                                                                owner=self)

        self._streefpeilAfwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                naam='streefpeilAfwaarts',
                                                label='streefpeil afwaarts',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OntwerpwaterstandStreefpeil.streefpeilAfwaarts',
                                                definition='Het gewenste waterpeil dat wordt nagestreefd aan de stroomafwaartse kant van het sluizen en/of stuwencomplex.',
                                                owner=self)

        self._streefpeilOpwaarts = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                naam='streefpeilOpwaarts',
                                                label='streefpeil opwaarts',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OntwerpwaterstandStreefpeil.streefpeilOpwaarts',
                                                definition='Het gewenste waterpeil dat wordt nagestreefd aan de stroomopwaartse kant van het sluizen en/of stuwencomplex.',
                                                owner=self)

    @property
    def relevanteOntwerpWaterstandAfwaarts(self) -> str:
        """De relevante ontwerpwaterstand afwaarts van de waterbouwkundige constructie."""
        return self._relevanteOntwerpWaterstandAfwaarts.get_waarde()

    @relevanteOntwerpWaterstandAfwaarts.setter
    def relevanteOntwerpWaterstandAfwaarts(self, value):
        self._relevanteOntwerpWaterstandAfwaarts.set_waarde(value, owner=self)

    @property
    def relevanteOntwerpWaterstandOpwaarts(self) -> str:
        """De relevante ontwerpwaterstand opwaarts van de waterbouwkundige constructie."""
        return self._relevanteOntwerpWaterstandOpwaarts.get_waarde()

    @relevanteOntwerpWaterstandOpwaarts.setter
    def relevanteOntwerpWaterstandOpwaarts(self, value):
        self._relevanteOntwerpWaterstandOpwaarts.set_waarde(value, owner=self)

    @property
    def streefpeilAfwaarts(self) -> KwantWrdInMeterTAWWaarden:
        """Het gewenste waterpeil dat wordt nagestreefd aan de stroomafwaartse kant van het sluizen en/of stuwencomplex."""
        return self._streefpeilAfwaarts.get_waarde()

    @streefpeilAfwaarts.setter
    def streefpeilAfwaarts(self, value):
        self._streefpeilAfwaarts.set_waarde(value, owner=self)

    @property
    def streefpeilOpwaarts(self) -> KwantWrdInMeterTAWWaarden:
        """Het gewenste waterpeil dat wordt nagestreefd aan de stroomopwaartse kant van het sluizen en/of stuwencomplex."""
        return self._streefpeilOpwaarts.get_waarde()

    @streefpeilOpwaarts.setter
    def streefpeilOpwaarts(self, value):
        self._streefpeilOpwaarts.set_waarde(value, owner=self)
