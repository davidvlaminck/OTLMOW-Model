# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorMerk(KeuzelijstField):
    """Keuzelijst met merken van contactoren volgens de fabrikanten."""
    naam = 'KlContactorMerk'
    label = 'Contactor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorMerk'
    definition = 'Keuzelijst met merken van contactoren volgens de fabrikanten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

