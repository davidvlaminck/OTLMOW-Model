# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOntwerpbelasting(KeuzelijstField):
    """De verschillende opties van ontwerpbelasting."""
    naam = 'KlOntwerpbelasting'
    label = 'Ontwerpbelasting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlOntwerpbelasting'
    definition = 'De verschillende opties van ontwerpbelasting.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntwerpbelasting'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

