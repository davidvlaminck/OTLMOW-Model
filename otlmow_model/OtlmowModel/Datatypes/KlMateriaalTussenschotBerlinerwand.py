# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTussenschotBerlinerwand(KeuzelijstField):
    """De mogelijke materialen van een tussenschot bij een Berlinerwand."""
    naam = 'KlMateriaalTussenschotBerlinerwand'
    label = 'Materiaal tussenschot Berlinerwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalTussenschotBerlinerwand'
    definition = 'De mogelijke materialen van een tussenschot bij een Berlinerwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTussenschotBerlinerwand'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

