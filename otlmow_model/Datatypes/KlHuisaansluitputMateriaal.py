# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHuisaansluitputMateriaal(KeuzelijstField):
    """Materialen voor een huisaansluitput."""
    naam = 'KlHuisaansluitputMateriaal'
    label = 'Huisaansluitput materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHuisaansluitputMateriaal'
    definition = 'Materialen voor een huisaansluitput.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHuisaansluitputMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='betonnen huisaansluitputje',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/beton'),
        'gres': KeuzelijstWaarde(invulwaarde='gres',
                                 label='gres',
                                 status='ingebruik',
                                 definitie='aansluitputje in grès.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/gres'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='kunstof aansluitputje',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/kunststof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

