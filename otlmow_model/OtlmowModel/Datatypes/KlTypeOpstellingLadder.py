# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeOpstellingLadder(KeuzelijstField):
    """Lijst met de verschillende opties voor de opstelling van een ladder."""
    naam = 'KlTypeOpstellingLadder'
    label = 'keuzelijst type opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeOpstellingLadder'
    definition = 'Lijst met de verschillende opties voor de opstelling van een ladder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeOpstellingLadder'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

