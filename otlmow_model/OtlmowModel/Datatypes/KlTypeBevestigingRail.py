# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBevestigingRail(KeuzelijstField):
    """Lijst met de verschillende types bevestiging van een rail."""
    naam = 'KlTypeBevestigingRail'
    label = 'Type bevestiging rail'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBevestigingRail'
    definition = 'Lijst met de verschillende types bevestiging van een rail.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBevestigingRail'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

