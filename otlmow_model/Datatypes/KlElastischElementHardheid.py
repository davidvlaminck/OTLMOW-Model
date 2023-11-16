# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElastischElementHardheid(KeuzelijstField):
    """Keuzelijst die de verschillende types hardheid van een elastisch element bevat."""
    naam = 'KlElastischElementHardheid'
    label = 'Elastisch element hardheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElastischElementHardheid'
    definition = 'Keuzelijst die de verschillende types hardheid van een elastisch element bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElastischElementHardheid'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

