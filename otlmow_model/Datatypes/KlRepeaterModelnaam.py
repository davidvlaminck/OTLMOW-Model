# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRepeaterModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Repeater."""
    naam = 'KlRepeaterModelnaam'
    label = 'repeater modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRepeaterModelnaam'
    definition = 'Keuzelijst met modelnamen voor Repeater.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRepeaterModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

