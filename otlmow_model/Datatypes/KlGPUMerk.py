# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGPUMerk(KeuzelijstField):
    """Het merk van de GPU."""
    naam = 'KlGPUMerk'
    label = 'GPU merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGPUMerk'
    definition = 'Het merk van de GPU.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGPUMerk'
    options = {
        'nvidia': KeuzelijstWaarde(invulwaarde='nvidia',
                                   label='Nvidia',
                                   status='ingebruik',
                                   definitie='Nvidia',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGPUMerk/nvidia')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

