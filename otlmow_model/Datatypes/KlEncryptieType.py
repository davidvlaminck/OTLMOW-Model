# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEncryptieType(KeuzelijstField):
    """Keuzelijst voor het type encryptie."""
    naam = 'KlEncryptieType'
    label = 'Encryptie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEncryptieType'
    definition = 'Keuzelijst voor het type encryptie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEncryptieType'
    options = {
        'mifare': KeuzelijstWaarde(invulwaarde='mifare',
                                   label='MIFARE',
                                   status='ingebruik',
                                   definitie='MIFARE',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEncryptieType/mifare'),
        'nedap': KeuzelijstWaarde(invulwaarde='nedap',
                                  label='NEDAP',
                                  status='ingebruik',
                                  definitie='NEDAP',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEncryptieType/nedap')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

