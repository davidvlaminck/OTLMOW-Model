# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHellingshoek(KeuzelijstField):
    """De hellingshoek in graden."""
    naam = 'KlHellingshoek'
    label = 'Hellingshoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHellingshoek'
    definition = 'De hellingshoek in graden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHellingshoek'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

