# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAflsuitingType(KeuzelijstField):
    """Het type van een afsluiting"""
    naam = 'KlAflsuitingType'
    label = 'Afsluiting type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAflsuitingType'
    definition = 'Het type van een afsluiting'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAflsuitingType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

