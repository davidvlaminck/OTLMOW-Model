# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsdeurTypeOpening(KeuzelijstField):
    """De mogelijke openingtypes van de toegangsdeur."""
    naam = 'KlToegangsdeurTypeOpening'
    label = 'Toegangsdeur type opening'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangsdeurTypeOpening'
    definition = 'De mogelijke openingtypes van de toegangsdeur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsdeurTypeOpening'
    options = {
        'binnendraaiend': KeuzelijstWaarde(invulwaarde='binnendraaiend',
                                           label='binnendraaiend',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsdeurTypeOpening/binnendraaiend'),
        'buitendraaiend': KeuzelijstWaarde(invulwaarde='buitendraaiend',
                                           label='buitendraaiend',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsdeurTypeOpening/buitendraaiend'),
        'schuivend': KeuzelijstWaarde(invulwaarde='schuivend',
                                      label='schuivend',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsdeurTypeOpening/schuivend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

