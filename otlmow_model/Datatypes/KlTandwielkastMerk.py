# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTandwielkastMerk(KeuzelijstField):
    """Lijst van merknamen van tandwielkasten volgens de fabrikant."""
    naam = 'KlTandwielkastMerk'
    label = 'Merknamen tandwielkasten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTandwielkastMerk'
    definition = 'Lijst van merknamen van tandwielkasten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTandwielkastMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

