# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandwerendeMaatregelen(KeuzelijstField):
    """Keuzelijst dat het brandwerenheidstype van de kokcercel terug geeft."""
    naam = 'KlBrandwerendeMaatregelen'
    label = 'Type brandwerendheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlBrandwerendeMaatregelen'
    definition = 'Keuzelijst dat het brandwerenheidstype van de kokcercel terug geeft.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandwerendeMaatregelen'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

