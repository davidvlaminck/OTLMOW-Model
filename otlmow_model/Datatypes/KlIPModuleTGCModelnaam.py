# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIPModuleTGCModelnaam(KeuzelijstField):
    """Lijst van modelnamen van IP-modules voor toegangscontrole volgens de fabrikant."""
    naam = 'KlIPModuleTGCModelnaam'
    label = 'Modelnamen IP-modules voor toegangscontroles'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIPModuleTGCModelnaam'
    definition = 'Lijst van modelnamen van IP-modules voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIPModuleTGCModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

