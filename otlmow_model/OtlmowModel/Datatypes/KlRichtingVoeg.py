# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRichtingVoeg(KeuzelijstField):
    """De richting van de voeg waarop de voegafdichting wordt geplaatst."""
    naam = 'KlRichtingVoeg'
    label = 'richting voeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRichtingVoeg'
    definition = 'De richting van de voeg waarop de voegafdichting wordt geplaatst.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRichtingVoeg'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

