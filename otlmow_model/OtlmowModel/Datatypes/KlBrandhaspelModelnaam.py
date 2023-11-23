# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandhaspelModelnaam(KeuzelijstField):
    """De modelnaam van de brandhaspel."""
    naam = 'KlBrandhaspelModelnaam'
    label = 'brandhaspel model naam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandhaspelModelnaam'
    definition = 'De modelnaam van de brandhaspel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandhaspelModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

