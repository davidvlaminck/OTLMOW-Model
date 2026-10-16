# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlModelnaamDebietmeter(KeuzelijstField):
    """De verschillende modelnamen van de debietmeter."""
    naam = 'KlModelnaamDebietmeter'
    label = 'Modelnaam debietmeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlModelnaamDebietmeter'
    definition = 'De verschillende modelnamen van de debietmeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlModelnaamDebietmeter'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

