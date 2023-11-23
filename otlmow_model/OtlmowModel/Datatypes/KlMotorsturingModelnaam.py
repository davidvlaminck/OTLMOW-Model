# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorsturingModelnaam(KeuzelijstField):
    """Lijst met modelnamen volgens de fabrikant voor technieken voor motorsturing in een laagspanningsinstallatie."""
    naam = 'KlMotorsturingModelnaam'
    label = 'Modelnamen motorsturing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorsturingModelnaam'
    definition = 'Lijst met modelnamen volgens de fabrikant voor technieken voor motorsturing in een laagspanningsinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorsturingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

