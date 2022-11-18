# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkRIS(KeuzelijstField):
    """Het merk van de RIS."""
    naam = 'KlIVRIMerkRIS'
    label = 'iVRIMerkRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkRIS'
    definition = 'Het merk van de RIS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkRIS'
    options = {
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkRIS/peek'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkRIS/swarco'),
        'swarco-nederland': KeuzelijstWaarde(invulwaarde='swarco-nederland',
                                             label='Swarco Nederland',
                                             status='ingebruik',
                                             definitie='Swarco Nederland',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkRIS/swarco-nederland')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

