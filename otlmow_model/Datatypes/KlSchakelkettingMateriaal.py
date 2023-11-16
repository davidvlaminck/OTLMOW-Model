# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


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
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

