# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleModelnaam'
    label = 'PT regelaarmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaarModule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

