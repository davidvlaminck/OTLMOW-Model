# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEWatergreppelType(KeuzelijstField):
    """Types van watergreppel."""
    naam = 'KlLEWatergreppelType'
    label = 'Watergreppel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEWatergreppelType'
    definition = 'Types van watergreppel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEWatergreppelType'
    options = {
        'type-II-A-2': KeuzelijstWaarde(invulwaarde='type-II-A-2',
                                        label='type II A 2',
                                        status='ingebruik',
                                        definitie='type II A 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-A-2'),
        'type-II-B-2': KeuzelijstWaarde(invulwaarde='type-II-B-2',
                                        label='type II B 2',
                                        status='ingebruik',
                                        definitie='type II B 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-B-2'),
        'type-II-C-2': KeuzelijstWaarde(invulwaarde='type-II-C-2',
                                        label='type II C 2',
                                        status='ingebruik',
                                        definitie='type II C 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-C-2'),
        'type-II-D-2': KeuzelijstWaarde(invulwaarde='type-II-D-2',
                                        label='type II D 2',
                                        status='ingebruik',
                                        definitie='type II D 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-D-2'),
        'type-II-E-2': KeuzelijstWaarde(invulwaarde='type-II-E-2',
                                        label='type II E 2',
                                        status='ingebruik',
                                        definitie='type II E 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEWatergreppelType/type-II-E-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

