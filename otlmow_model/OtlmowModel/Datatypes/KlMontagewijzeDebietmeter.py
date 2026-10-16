# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMontagewijzeDebietmeter(KeuzelijstField):
    """De verschillende montagewijzes van de debietmeter."""
    naam = 'KlMontagewijzeDebietmeter'
    label = 'Montagewijze debietmeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMontagewijzeDebietmeter'
    definition = 'De verschillende montagewijzes van de debietmeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMontagewijzeDebietmeter'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

