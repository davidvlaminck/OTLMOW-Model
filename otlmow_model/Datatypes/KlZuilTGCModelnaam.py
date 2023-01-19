# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZuilTGCModelnaam(KeuzelijstField):
    """Lijst van modelnamen van zuilen voor toegangscontrole volgens de fabrikant."""
    naam = 'KlZuilTGCModelnaam'
    label = 'Modelnamen zuilen toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZuilTGCModelnaam'
    definition = 'Lijst van modelnamen van zuilen voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZuilTGCModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

