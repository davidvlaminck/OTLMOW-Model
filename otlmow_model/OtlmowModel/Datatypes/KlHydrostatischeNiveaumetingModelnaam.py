# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrostatischeNiveaumetingModelnaam(KeuzelijstField):
    """Modelnamen van de hydrostatische niveaumeting."""
    naam = 'KlHydrostatischeNiveaumetingModelnaam'
    label = 'Hydrostatische niveaumeting modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrostatischeNiveaumetingModelnaam'
    definition = 'Modelnamen van de hydrostatische niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrostatischeNiveaumetingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

