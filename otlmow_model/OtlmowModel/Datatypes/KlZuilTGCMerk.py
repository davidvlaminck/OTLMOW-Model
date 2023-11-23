# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZuilTGCMerk(KeuzelijstField):
    """Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant."""
    naam = 'KlZuilTGCMerk'
    label = 'Merknamen zuilen toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZuilTGCMerk'
    definition = 'Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZuilTGCMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

