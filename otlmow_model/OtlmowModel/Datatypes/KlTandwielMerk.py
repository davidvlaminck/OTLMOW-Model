# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTandwielMerk(KeuzelijstField):
    """De keuzelijst die de namen van de merken van het tandwiel bevat."""
    naam = 'KlTandwielMerk'
    label = 'Tandwiel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTandwielMerk'
    definition = 'De keuzelijst die de namen van de merken van het tandwiel bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTandwielMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

