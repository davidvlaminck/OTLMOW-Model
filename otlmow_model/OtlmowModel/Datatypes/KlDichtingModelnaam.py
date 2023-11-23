# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDichtingModelnaam(KeuzelijstField):
    """Lijst met modelnamen van dichtingen volgens de fabrikant."""
    naam = 'KlDichtingModelnaam'
    label = 'Modelnaam dichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDichtingModelnaam'
    definition = 'Lijst met modelnamen van dichtingen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDichtingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

