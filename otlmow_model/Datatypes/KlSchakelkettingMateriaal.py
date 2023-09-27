# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchakelkettingMateriaal(KeuzelijstField):
    """Keuzelijst die de mogelijke materialen van een schakelketting bevat."""
    naam = 'KlSchakelkettingMateriaal'
    label = 'Schakelketting materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchakelkettingMateriaal'
    definition = 'Keuzelijst die de mogelijke materialen van een schakelketting bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchakelkettingMateriaal'
    options = {
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelkettingMateriaal/rvs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

