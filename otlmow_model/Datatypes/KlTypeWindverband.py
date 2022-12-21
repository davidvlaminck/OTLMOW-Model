# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWindverband(KeuzelijstField):
    """Het type windverband."""
    naam = 'KlTypeWindverband'
    label = 'Type windverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeWindverband'
    definition = 'Het type windverband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWindverband'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

