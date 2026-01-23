# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringRandafwerking(KeuzelijstField):
    """De lijst met verschillende types uitvoering van de randafwerking."""
    naam = 'KlUitvoeringRandafwerking'
    label = 'uitvoering randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlUitvoeringRandafwerking'
    definition = 'De lijst met verschillende types uitvoering van de randafwerking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringRandafwerking'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

