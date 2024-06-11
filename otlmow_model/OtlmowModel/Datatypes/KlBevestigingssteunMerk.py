# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingssteunMerk(KeuzelijstField):
    """De mogelijke merken of fabrikanten van een bevestigingssteun."""
    naam = 'KlBevestigingssteunMerk'
    label = 'Bevestigingssteun merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingssteunMerk'
    definition = 'De mogelijke merken of fabrikanten van een bevestigingssteun.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingssteunMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

