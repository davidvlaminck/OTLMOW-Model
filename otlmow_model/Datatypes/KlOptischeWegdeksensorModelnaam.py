# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOptischeWegdeksensorModelnaam(KeuzelijstField):
    """Optische wegdeksensor modelnamen."""
    naam = 'KlOptischeWegdeksensorModelnaam'
    label = 'Optische wegdeksensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOptischeWegdeksensorModelnaam'
    definition = 'Optische wegdeksensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOptischeWegdeksensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

