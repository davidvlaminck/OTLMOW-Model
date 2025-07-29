# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeMechanisme(KeuzelijstField):
    """Lijst met de verschillende types mechanismen."""
    naam = 'KlTypeMechanisme'
    label = 'Type mechanisme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeMechanisme'
    definition = 'Lijst met de verschillende types mechanismen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeMechanisme'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

