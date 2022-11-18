# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIORichting(KeuzelijstField):
    """Geeft aan of de IO-kaart dient voor input of output."""
    naam = 'KlIORichting'
    label = 'IO richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIORichting'
    definition = 'Geeft aan of de IO-kaart dient voor input of output.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIORichting'
    options = {
        'input': KeuzelijstWaarde(invulwaarde='input',
                                  label='input',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/input'),
        'output': KeuzelijstWaarde(invulwaarde='output',
                                   label='output',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/output')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

