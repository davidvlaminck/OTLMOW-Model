# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBAZModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor VRBAZ."""
    naam = 'KlVRBAZModelnaam'
    label = 'VR-BAZ modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBAZModelnaam'
    definition = 'Keuzelijst met modelnamen voor VRBAZ.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBAZModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

