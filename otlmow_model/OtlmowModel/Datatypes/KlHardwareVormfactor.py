# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareVormfactor(KeuzelijstField):
    """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
    naam = 'KlHardwareVormfactor'
    label = 'Hardware vormfactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareVormfactor'
    definition = 'Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareVormfactor'
    options = {
        'desktop': KeuzelijstWaarde(invulwaarde='desktop',
                                    label='desktop',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/desktop'),
        'laptop': KeuzelijstWaarde(invulwaarde='laptop',
                                   label='laptop',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/laptop'),
        'server': KeuzelijstWaarde(invulwaarde='server',
                                   label='server',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareVormfactor/server')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

