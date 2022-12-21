# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTrekdraadEncoderNiveaumetingModelnaam(KeuzelijstField):
    """Modelnamen van de trekdraad encoder niveaumeting."""
    naam = 'KlTrekdraadEncoderNiveaumetingModelnaam'
    label = 'Trekdraad encoder niveaumeting modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTrekdraadEncoderNiveaumetingModelnaam'
    definition = 'Modelnamen van de trekdraad encoder niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTrekdraadEncoderNiveaumetingModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

