# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpectrum(KeuzelijstField):
    """Mogelijke spectra"""
    naam = 'KlSpectrum'
    label = 'Spectrum'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpectrum'
    definition = 'Mogelijke spectra'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpectrum'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

