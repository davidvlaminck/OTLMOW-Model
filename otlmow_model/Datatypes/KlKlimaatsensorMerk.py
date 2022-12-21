# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlimaatsensorMerk(KeuzelijstField):
    """Merknamen voor klimaatsensoren"""
    naam = 'KlKlimaatsensorMerk'
    label = 'Klimaatsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKlimaatsensorMerk'
    definition = 'Merknamen voor klimaatsensoren'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlimaatsensorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

