# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOpeningswijze(KeuzelijstField):
    """De mogelijke manieren om een object te openen."""
    naam = 'KlOpeningswijze'
    label = 'Openingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOpeningswijze'
    definition = 'De mogelijke manieren om een object te openen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOpeningswijze'
    options = {
        'demonterend': KeuzelijstWaarde(invulwaarde='demonterend',
                                        label='demonterend',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOpeningswijze/demonterend'),
        'scharnierend': KeuzelijstWaarde(invulwaarde='scharnierend',
                                         label='scharnierend',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOpeningswijze/scharnierend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

