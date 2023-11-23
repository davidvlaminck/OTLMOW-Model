# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangspoortModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor allerlei types van toegangspoorten volgens de fabrikant"""
    naam = 'KlToegangspoortModelnaam'
    label = 'Toegangspoort modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangspoortModelnaam'
    definition = 'Lijst met modelnamen voor allerlei types van toegangspoorten volgens de fabrikant'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangspoortModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

