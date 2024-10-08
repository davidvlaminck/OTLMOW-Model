# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElektromotorBeschermingsgraad(KeuzelijstField):
    """De beschmeringsgraad van een elektromotor, uitgerdukt als 'IP', gevolgd door 2 cijfers."""
    naam = 'KlElektromotorBeschermingsgraad'
    label = 'Elektromotor beschermingsgraad'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElektromotorBeschermingsgraad'
    definition = "De beschmeringsgraad van een elektromotor, uitgerdukt als 'IP', gevolgd door 2 cijfers."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElektromotorBeschermingsgraad'
    options = {
        'ip20': KeuzelijstWaarde(invulwaarde='ip20',
                                 label='IP20',
                                 status='ingebruik',
                                 definitie='IP20',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBeschermingsgraad/ip20'),
        'ip24': KeuzelijstWaarde(invulwaarde='ip24',
                                 label='IP24',
                                 status='ingebruik',
                                 definitie='IP24',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBeschermingsgraad/ip24'),
        'ip54': KeuzelijstWaarde(invulwaarde='ip54',
                                 label='IP54',
                                 status='ingebruik',
                                 definitie='IP54',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBeschermingsgraad/ip54')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

