# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorbeveiligingModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor motorbeveiligingen volgens de fabrikant."""
    naam = 'KlMotorbeveiligingModelnaam'
    label = 'Modelnamen motorbeveiligingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorbeveiligingModelnaam'
    definition = 'Lijst met modelnamen voor motorbeveiligingen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorbeveiligingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

