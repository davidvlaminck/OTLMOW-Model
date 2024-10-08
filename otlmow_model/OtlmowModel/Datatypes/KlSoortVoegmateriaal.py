# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSoortVoegmateriaal(KeuzelijstField):
    """De mogelijke soorten van voegmateriaal."""
    naam = 'KlSoortVoegmateriaal'
    label = 'Soort voegmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSoortVoegmateriaal'
    definition = 'De mogelijke soorten van voegmateriaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSoortVoegmateriaal'
    options = {
        'asfalt': KeuzelijstWaarde(invulwaarde='asfalt',
                                   label='asfalt',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoortVoegmateriaal/asfalt'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoortVoegmateriaal/beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

