# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTandwielModelnaam(KeuzelijstField):
    """De keuzelijst die de modelnamen van het tandwiel bevat."""
    naam = 'KlTandwielModelnaam'
    label = 'Tandwiel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTandwielModelnaam'
    definition = 'De keuzelijst die de modelnamen van het tandwiel bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTandwielModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

