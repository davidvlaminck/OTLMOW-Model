# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBypassSchakelaarLocatie(KeuzelijstField):
    """De mogelijke locaties van een bypass schakelaar."""
    naam = 'KlBypassSchakelaarLocatie'
    label = 'Bypass schakelaar locatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBypassSchakelaarLocatie'
    definition = 'De mogelijke locaties van een bypass schakelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBypassSchakelaarLocatie'
    options = {
        'laagspanningsbord': KeuzelijstWaarde(invulwaarde='laagspanningsbord',
                                              label='Laagspanningsbord',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBypassSchakelaarLocatie/laagspanningsbord'),
        'ups': KeuzelijstWaarde(invulwaarde='ups',
                                label='UPS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBypassSchakelaarLocatie/ups')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

