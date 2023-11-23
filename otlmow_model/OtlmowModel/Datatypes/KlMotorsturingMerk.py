# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorsturingMerk(KeuzelijstField):
    """Lijst met merknamen volgens de fabrikant voor technieken voor motorsturing in een laagspanningsinstallatie."""
    naam = 'KlMotorsturingMerk'
    label = 'Merken motorsturing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorsturingMerk'
    definition = 'Lijst met merknamen volgens de fabrikant voor technieken voor motorsturing in een laagspanningsinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorsturingMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

