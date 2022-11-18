# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemModelnaam(KeuzelijstField):
    """Lijst met mogelijke modelnamen voor fietstelsystemen."""
    naam = 'KlFietstelsysteemModelnaam'
    label = 'Modelnaam fietstelsysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemModelnaam'
    definition = 'Lijst met mogelijke modelnamen voor fietstelsystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemModelnaam'
    options = {
        'eco-combo-2': KeuzelijstWaarde(invulwaarde='eco-combo-2',
                                        label='eco-combo 2',
                                        status='ingebruik',
                                        definitie='eco-combo 2',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFietstelsysteemModelnaam/eco-combo-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

