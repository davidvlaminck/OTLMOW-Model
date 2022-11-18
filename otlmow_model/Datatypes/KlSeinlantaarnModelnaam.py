# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Seinlantaarn."""
    naam = 'KlSeinlantaarnModelnaam'
    label = 'seinlantaarn modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnModelnaam'
    definition = 'Keuzelijst met modelnamen voor Seinlantaarn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

