# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestelventilatorFilterdoekMateriaal(KeuzelijstField):
    """Keuzelijst die de verschillende materialen bevat waaruit de filterdoek van een toestelventilator vervaardigd kan zijn."""
    naam = 'KlToestelventilatorFilterdoekMateriaal'
    label = 'Toestelventilator filterdoek materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToestelventilatorFilterdoekMateriaal'
    definition = 'Keuzelijst die de verschillende materialen bevat waaruit de filterdoek van een toestelventilator vervaardigd kan zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestelventilatorFilterdoekMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

