# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneConstructiefType(KeuzelijstField):
    """Het constructief type van een antenne bepaalt de vorm en de wijze van ophanging."""
    naam = 'KlAntenneConstructiefType'
    label = 'Antenne constructief type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneConstructiefType'
    definition = 'Het constructief type van een antenne bepaalt de vorm en de wijze van ophanging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneConstructiefType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

