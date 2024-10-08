# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBolder(KeuzelijstField):
    """De mogelijke materialen van een bolder."""
    naam = 'KlMateriaalBolder'
    label = 'Materiaal bolder.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalBolder'
    definition = 'De mogelijke materialen van een bolder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBolder'
    options = {
        'gietijzer': KeuzelijstWaarde(invulwaarde='gietijzer',
                                      label='gietijzer',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBolder/gietijzer'),
        'roestvaststaal': KeuzelijstWaarde(invulwaarde='roestvaststaal',
                                           label='roestvaststaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBolder/roestvaststaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBolder/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

