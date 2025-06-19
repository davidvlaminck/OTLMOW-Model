# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankModelnaam(KeuzelijstField):
    """De modelnaam van de tank."""
    naam = 'KlTankModelnaam'
    label = 'tank modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankModelnaam'
    definition = 'De modelnaam van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankModelnaam'
    options = {
        '24l-10b': KeuzelijstWaarde(invulwaarde='24l-10b',
                                    label='24L/10B',
                                    status='ingebruik',
                                    definitie='24L/10B',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankModelnaam/24l-10b')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

