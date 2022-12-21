# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLockermanagementmoduleModelnaam(KeuzelijstField):
    """Modelnaam van een lockermanagementmodule."""
    naam = 'KlLockermanagementmoduleModelnaam'
    label = 'Lockermanagamentmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLockermanagementmoduleModelnaam'
    definition = 'Modelnaam van een lockermanagementmodule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLockermanagementmoduleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

