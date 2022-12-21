# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalfilterModelnaam(KeuzelijstField):
    """De modelnaam van een signaalfilter."""
    naam = 'KlSignaalfilterModelnaam'
    label = 'Signaalfilter modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalfilterModelnaam'
    definition = 'De modelnaam van een signaalfilter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalfilterModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

