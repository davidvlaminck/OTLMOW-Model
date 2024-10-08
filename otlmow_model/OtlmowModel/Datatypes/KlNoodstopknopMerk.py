# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodstopknopMerk(KeuzelijstField):
    """Het merk van een noodstopknop."""
    naam = 'KlNoodstopknopMerk'
    label = 'Noodstopknop merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodstopknopMerk'
    definition = 'Het merk van een noodstopknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodstopknopMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

