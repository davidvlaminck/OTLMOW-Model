# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimatisatieModelnaam(KeuzelijstField):
    """Modelnamen voor klimatisatiesystemen."""
    naam = 'KlKlimatisatieModelnaam'
    label = 'Klimatisatie modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimatisatieModelnaam'
    definition = 'Modelnamen voor klimatisatiesystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimatisatieModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

