# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtebegrenzerMerk(KeuzelijstField):
    """De mogelijke merken van een hoogtebegrenzer."""
    naam = 'KlHoogtebegrenzerMerk'
    label = 'Hoogtebegrenzer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtebegrenzerMerk'
    definition = 'De mogelijke merken van een hoogtebegrenzer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtebegrenzerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

