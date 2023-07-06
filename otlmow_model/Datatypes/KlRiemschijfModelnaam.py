# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRiemschijfModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen van de riemschijf."""
    naam = 'KlRiemschijfModelnaam'
    label = 'Riemschijf modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRiemschijfModelnaam'
    definition = 'Keuzelijst met modelnamen van de riemschijf.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRiemschijfModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

