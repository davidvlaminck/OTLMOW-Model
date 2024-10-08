# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDolomietType(KeuzelijstField):
    """Types van dolomiet."""
    naam = 'KlDolomietType'
    label = 'Dolomiet type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDolomietType'
    definition = 'Types van dolomiet.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDolomietType'
    options = {
        '0-15': KeuzelijstWaarde(invulwaarde='0-15',
                                 label='0-15',
                                 status='ingebruik',
                                 definitie='0/15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-15'),
        '0-5': KeuzelijstWaarde(invulwaarde='0-5',
                                label='0-5',
                                status='ingebruik',
                                definitie='0/5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/0-5'),
        '5-15': KeuzelijstWaarde(invulwaarde='5-15',
                                 label='5-15',
                                 status='ingebruik',
                                 definitie='mei-15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDolomietType/5-15')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

