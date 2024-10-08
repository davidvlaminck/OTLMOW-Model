# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingKaliber(KeuzelijstField):
    """De mogelijke kalibers."""
    naam = 'KlBestrijkingKaliber'
    label = 'kalibers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingKaliber'
    definition = 'De mogelijke kalibers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingKaliber'
    options = {
        '2-10': KeuzelijstWaarde(invulwaarde='2-10',
                                 label='2/10',
                                 status='ingebruik',
                                 definitie='kaliber 2/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-10'),
        '2-4': KeuzelijstWaarde(invulwaarde='2-4',
                                label='2/4',
                                status='ingebruik',
                                definitie='kaliber 2/4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-4'),
        '2-6.3': KeuzelijstWaarde(invulwaarde='2-6.3',
                                  label='2/6.3',
                                  status='ingebruik',
                                  definitie='kaliber 2/6.3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-6.3'),
        '4-10': KeuzelijstWaarde(invulwaarde='4-10',
                                 label='4/10',
                                 status='ingebruik',
                                 definitie='kaliber 4/10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-10'),
        '4-6.3': KeuzelijstWaarde(invulwaarde='4-6.3',
                                  label='4/6.3',
                                  status='ingebruik',
                                  definitie='kaliber 4/6.3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-6.3'),
        '6.3-10': KeuzelijstWaarde(invulwaarde='6.3-10',
                                   label='6.3/10',
                                   status='ingebruik',
                                   definitie='kaliber 6.3/10',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/6.3-10')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

