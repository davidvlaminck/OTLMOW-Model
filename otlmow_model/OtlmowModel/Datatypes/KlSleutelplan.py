# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSleutelplan(KeuzelijstField):
    """Een keuzelijst met verschillende types van sleutel."""
    naam = 'KlSleutelplan'
    label = 'Sleutelplan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSleutelplan'
    definition = 'Een keuzelijst met verschillende types van sleutel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSleutelplan'
    options = {
        'dender': KeuzelijstWaarde(invulwaarde='dender',
                                   label='dender',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/dender'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                     label='digitaal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/digitaal'),
        'isio': KeuzelijstWaarde(invulwaarde='isio',
                                 label='isio',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/isio'),
        'type-a': KeuzelijstWaarde(invulwaarde='type-a',
                                   label='type A',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/type-a'),
        'type-b': KeuzelijstWaarde(invulwaarde='type-b',
                                   label='type B',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/type-b'),
        'uniek': KeuzelijstWaarde(invulwaarde='uniek',
                                  label='uniek',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/uniek'),
        'yale-5': KeuzelijstWaarde(invulwaarde='yale-5',
                                   label='yale 5',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleutelplan/yale-5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

