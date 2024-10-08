# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorModelnaam(KeuzelijstField):
    """De modelnaam van de afmetingsensor."""
    naam = 'KlAfmetingsensorModelnaam'
    label = 'Afmetingsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorModelnaam'
    definition = 'De modelnaam van de afmetingsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorModelnaam'
    options = {
        'FPS': KeuzelijstWaarde(invulwaarde='FPS',
                                label='FPS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/FPS'),
        'LMS': KeuzelijstWaarde(invulwaarde='LMS',
                                label='LMS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorModelnaam/LMS')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

