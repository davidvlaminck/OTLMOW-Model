# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBadgelezerModelnaam(KeuzelijstField):
    """Lijst van modelnamen voor badgelezers volgens de fabrikant."""
    naam = 'KlBadgelezerModelnaam'
    label = 'Modelnamen badgelezers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBadgelezerModelnaam'
    definition = 'Lijst van modelnamen voor badgelezers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBadgelezerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

