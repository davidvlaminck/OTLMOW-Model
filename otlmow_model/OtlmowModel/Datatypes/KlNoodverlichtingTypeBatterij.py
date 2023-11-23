# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodverlichtingTypeBatterij(KeuzelijstField):
    """De verschillende types van batterijen voor een noodverlichting."""
    naam = 'KlNoodverlichtingTypeBatterij'
    label = 'Noodverlichting type batterij'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodverlichtingTypeBatterij'
    definition = 'De verschillende types van batterijen voor een noodverlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodverlichtingTypeBatterij'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

