# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlControlepaneelMerk(KeuzelijstField):
    """Het merk van het controlepaneel"""
    naam = 'KlControlepaneelMerk'
    label = 'Controlepaneel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlControlepaneelMerk'
    definition = 'Het merk van het controlepaneel'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlControlepaneelMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

