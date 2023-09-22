# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPMUMerk(KeuzelijstField):
    """Power management unit merken."""
    naam = 'KlPMUMerk'
    label = 'Power management unit merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPMUMerk'
    definition = 'Power management unit merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPMUMerk'
    options = {
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPMUMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

