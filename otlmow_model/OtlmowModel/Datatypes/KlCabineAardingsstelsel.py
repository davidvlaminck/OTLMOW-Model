# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineAardingsstelsel(KeuzelijstField):
    """Lijst van mogelijke aardinggsstelsels."""
    naam = 'KlCabineAardingsstelsel'
    label = 'Cabine aardingsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineAardingsstelsel'
    definition = 'Lijst van mogelijke aardinggsstelsels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineAardingsstelsel'
    options = {
        'gescheiden': KeuzelijstWaarde(invulwaarde='gescheiden',
                                       label='gescheiden',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/gescheiden'),
        'globaal': KeuzelijstWaarde(invulwaarde='globaal',
                                    label='globaal',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineAardingsstelsel/globaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

