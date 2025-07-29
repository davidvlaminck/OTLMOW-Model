# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTaatsmechanisme(KeuzelijstField):
    """Lijst met de verschillende materialen van een taatsmechanisme."""
    naam = 'KlMateriaalTaatsmechanisme'
    label = 'Materiaal taatsmechanisme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalTaatsmechanisme'
    definition = 'Lijst met de verschillende materialen van een taatsmechanisme.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTaatsmechanisme'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

