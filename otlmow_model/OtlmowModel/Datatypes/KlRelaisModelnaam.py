# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRelaisModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor relais volgens de fabrikant."""
    naam = 'KlRelaisModelnaam'
    label = 'Modelnamen relais'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRelaisModelnaam'
    definition = 'Lijst met modelnamen voor relais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRelaisModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

