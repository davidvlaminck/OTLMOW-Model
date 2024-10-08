# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantstrookType(KeuzelijstField):
    """Types van kantstrook."""
    naam = 'KlLEKantstrookType'
    label = 'Kantstrook type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantstrookType'
    definition = 'Types van kantstrook.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantstrookType'
    options = {
        'type-II-A-1': KeuzelijstWaarde(invulwaarde='type-II-A-1',
                                        label='type II A 1',
                                        status='ingebruik',
                                        definitie='type II A 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-A-1'),
        'type-II-B-1': KeuzelijstWaarde(invulwaarde='type-II-B-1',
                                        label='type II B 1',
                                        status='ingebruik',
                                        definitie='type II B 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-B-1'),
        'type-II-C-1': KeuzelijstWaarde(invulwaarde='type-II-C-1',
                                        label='type II C 1',
                                        status='ingebruik',
                                        definitie='type II C 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-C-1'),
        'type-II-D-1': KeuzelijstWaarde(invulwaarde='type-II-D-1',
                                        label='type II D 1',
                                        status='ingebruik',
                                        definitie='type II D 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-D-1'),
        'type-II-E-1': KeuzelijstWaarde(invulwaarde='type-II-E-1',
                                        label='type II E 1',
                                        status='ingebruik',
                                        definitie='type II E 1',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantstrookType/type-II-E-1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

