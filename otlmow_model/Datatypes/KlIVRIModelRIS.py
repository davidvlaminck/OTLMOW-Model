# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelRIS(KeuzelijstField):
    """De modelnaam van de RIS."""
    naam = 'KlIVRIModelRIS'
    label = 'iVRIModelRIS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelRIS'
    definition = 'De modelnaam van de RIS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelRIS'
    options = {
        'cloudris': KeuzelijstWaarde(invulwaarde='cloudris',
                                     label='CloudRIS',
                                     status='ingebruik',
                                     definitie='CloudRIS',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelRIS/cloudris'),
        'virtualacu': KeuzelijstWaarde(invulwaarde='virtualacu',
                                       label='VirtualACU',
                                       status='ingebruik',
                                       definitie='VirtualACU',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelRIS/virtualacu')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

