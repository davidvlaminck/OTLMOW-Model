# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitingDamwandBestaandeConstructie(KeuzelijstField):
    """De aansluiting van de damwand op een bestaande constructie."""
    naam = 'KlAansluitingDamwandBestaandeConstructie'
    label = 'Aansluiting damwand bestaande constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitingDamwandBestaandeConstructie'
    definition = 'De aansluiting van de damwand op een bestaande constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitingDamwandBestaandeConstructie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

