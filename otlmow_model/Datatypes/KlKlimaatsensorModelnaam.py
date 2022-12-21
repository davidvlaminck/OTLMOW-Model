# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimaatsensorModelnaam(KeuzelijstField):
    """Modelnamen volgens de fabrikant voor klimaatsensoren"""
    naam = 'KlKlimaatsensorModelnaam'
    label = 'Klimaatsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimaatsensorModelnaam'
    definition = 'Modelnamen volgens de fabrikant voor klimaatsensoren'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimaatsensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

