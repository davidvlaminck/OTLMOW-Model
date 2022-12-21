# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurmoduleTGCModelnaam(KeuzelijstField):
    """Lijst van modelnamen van deurmodules voor toegangscontrole volgens de fabrikant."""
    naam = 'KlDeurmoduleTGCModelnaam'
    label = 'Modelnamen deurmodules'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDeurmoduleTGCModelnaam'
    definition = 'Lijst van modelnamen van deurmodules voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurmoduleTGCModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

