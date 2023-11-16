# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZendontvangerMerk(KeuzelijstField):
    """Lijst van merknamen van zendontvangers volgens de fabrikant."""
    naam = 'KlZendontvangerMerk'
    label = 'Zendontvanger merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZendontvangerMerk'
    definition = 'Lijst van merknamen van zendontvangers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZendontvangerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

