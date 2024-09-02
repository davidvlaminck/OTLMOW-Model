# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVastAanslagmateriaal(KeuzelijstField):
    """De mogelijke materialen voor een aanslagprofiel."""
    naam = 'KlVastAanslagmateriaal'
    label = 'Aanslagprofiel materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVastAanslagmateriaal'
    definition = 'De mogelijke materialen voor een aanslagprofiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVastAanslagmateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastAanslagmateriaal/beton'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastAanslagmateriaal/hout'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='natuursteen',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastAanslagmateriaal/natuursteen'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastAanslagmateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

