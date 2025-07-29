# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeDoorsnede(KeuzelijstField):
    """Type doorsnede van de ligger."""
    naam = 'KlTypeDoorsnede'
    label = 'type doorsnede'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeDoorsnede'
    definition = 'Type doorsnede van de ligger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeDoorsnede'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

