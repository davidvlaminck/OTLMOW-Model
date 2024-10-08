# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieDrassigheid(KeuzelijstField):
    """De mate van drassigheid.."""
    naam = 'KlVegetatieDrassigheid'
    label = 'Vegetatie drassigheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieDrassigheid'
    definition = 'De mate van drassigheid..'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieDrassigheid'
    options = {
        'matig-drassig': KeuzelijstWaarde(invulwaarde='matig-drassig',
                                          label='matig drassig',
                                          status='ingebruik',
                                          definitie='De ondergrond is matig drassig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/matig-drassig'),
        'niet-drassig': KeuzelijstWaarde(invulwaarde='niet-drassig',
                                         label='niet drassig',
                                         status='ingebruik',
                                         definitie='De ondergrond is niet drassig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/niet-drassig'),
        'sterk-drassig': KeuzelijstWaarde(invulwaarde='sterk-drassig',
                                          label='sterk drassig',
                                          status='ingebruik',
                                          definitie='De ondergrond is sterk drassig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieDrassigheid/sterk-drassig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

