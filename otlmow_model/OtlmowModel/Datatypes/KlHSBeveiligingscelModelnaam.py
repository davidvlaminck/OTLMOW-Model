# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelModelnaam(KeuzelijstField):
    """De modelnaam van de HS-beveiligingscel."""
    naam = 'KlHSBeveiligingscelModelnaam'
    label = 'HS-beveiligingscel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelModelnaam'
    definition = 'De modelnaam van de HS-beveiligingscel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

