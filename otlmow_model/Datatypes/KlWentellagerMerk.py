# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWentellagerMerk(KeuzelijstField):
    """Lijst van merknamen van wentellagers volgens de fabrikant."""
    naam = 'KlWentellagerMerk'
    label = 'Wentellager merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWentellagerMerk'
    definition = 'Lijst van merknamen van wentellagers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWentellagerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

