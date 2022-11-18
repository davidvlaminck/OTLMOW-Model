# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAswegersiteTypeMarkering(KeuzelijstField):
    """Lijst met mogelijke types van markeringen bij een aswegersite."""
    naam = 'KlAswegersiteTypeMarkering'
    label = 'Type markering aswegersite'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAswegersiteTypeMarkering'
    definition = 'Lijst met mogelijke types van markeringen bij een aswegersite.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAswegersiteTypeMarkering'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

