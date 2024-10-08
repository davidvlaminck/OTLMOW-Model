# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankOpstelling(KeuzelijstField):
    """De opstelling van de tank."""
    naam = 'KlTankOpstelling'
    label = 'Tank opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankOpstelling'
    definition = 'De opstelling van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankOpstelling'
    options = {
        'liggend': KeuzelijstWaarde(invulwaarde='liggend',
                                    label='liggend',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankOpstelling/liggend'),
        'staand': KeuzelijstWaarde(invulwaarde='staand',
                                   label='staand',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankOpstelling/staand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

