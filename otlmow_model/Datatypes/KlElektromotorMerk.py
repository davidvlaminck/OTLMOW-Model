# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElektromotorMerk(KeuzelijstField):
    """Het merk van een elektromotor."""
    naam = 'KlElektromotorMerk'
    label = 'Elektromotor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElektromotorMerk'
    definition = 'Het merk van een elektromotor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElektromotorMerk'
    options = {
        'abb': KeuzelijstWaarde(invulwaarde='abb',
                                label='ABB',
                                status='ingebruik',
                                definitie='ABB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorMerk/abb'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorMerk/siemens'),
        'vem': KeuzelijstWaarde(invulwaarde='vem',
                                label='VEM',
                                status='ingebruik',
                                definitie='VEM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorMerk/vem')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

