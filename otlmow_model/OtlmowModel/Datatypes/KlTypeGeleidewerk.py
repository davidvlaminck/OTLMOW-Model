# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGeleidewerk(KeuzelijstField):
    """De verschillende types van geleidewerk."""
    naam = 'KlTypeGeleidewerk'
    label = 'Types geleidewerk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeGeleidewerk'
    definition = 'De verschillende types van geleidewerk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGeleidewerk'
    options = {
        'drijvend': KeuzelijstWaarde(invulwaarde='drijvend',
                                     label='drijvend',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGeleidewerk/drijvend'),
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='vast',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGeleidewerk/vast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

