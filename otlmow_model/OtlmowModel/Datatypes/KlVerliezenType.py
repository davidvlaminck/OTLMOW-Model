# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerliezenType(KeuzelijstField):
    """Aanduiding van het type verliezen."""
    naam = 'KlVerliezenType'
    label = 'Type verliezen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerliezenType'
    definition = 'Aanduiding van het type verliezen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerliezenType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

