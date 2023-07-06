# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGlijlagerModelnaam(KeuzelijstField):
    """Lijst met modelnamen van glijlagers volgens de fabrikant."""
    naam = 'KlGlijlagerModelnaam'
    label = 'Modelnamen van glijlagers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGlijlagerModelnaam'
    definition = 'Lijst met modelnamen van glijlagers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGlijlagerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

