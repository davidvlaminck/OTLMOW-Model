# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerModelnaam(KeuzelijstField):
    """De modelnaam van de omvormer."""
    naam = 'KlOmvormerModelnaam'
    label = 'Omvormer modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerModelnaam'
    definition = 'De modelnaam van de omvormer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerModelnaam'
    options = {
        'c4l6400-eoc-p': KeuzelijstWaarde(invulwaarde='c4l6400-eoc-p',
                                          label='C4L6400 EOC P',
                                          status='ingebruik',
                                          definitie='C4L6400 EOC P',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerModelnaam/c4l6400-eoc-p'),
        'kc-300d-c': KeuzelijstWaarde(invulwaarde='kc-300d-c',
                                      label='KC 300D C',
                                      status='ingebruik',
                                      definitie='KC300D C',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerModelnaam/kc-300d-c')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

