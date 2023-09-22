# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRiemschijfMerk(KeuzelijstField):
    """Keuzelijst van merknamen van de riemschijf."""
    naam = 'KlRiemschijfMerk'
    label = 'Riemschijf merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRiemschijfMerk'
    definition = 'Keuzelijst van merknamen van de riemschijf.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRiemschijfMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

