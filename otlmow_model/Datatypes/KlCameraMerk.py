# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraMerk(KeuzelijstField):
    """Het merk van de camera."""
    naam = 'KlCameraMerk'
    label = 'Camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraMerk'
    definition = 'Het merk van de camera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraMerk'
    options = {
        'axis': KeuzelijstWaarde(invulwaarde='axis',
                                 label='Axis',
                                 status='ingebruik',
                                 definitie='Axis',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/axis'),
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/bosch'),
        'mobotix': KeuzelijstWaarde(invulwaarde='mobotix',
                                    label='Mobotix',
                                    status='ingebruik',
                                    definitie='Mobotix',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/mobotix'),
        'teledyne-flir': KeuzelijstWaarde(invulwaarde='teledyne-flir',
                                          label='Teledyne FLIR',
                                          status='ingebruik',
                                          definitie='Teledyne FLIR',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/teledyne-flir'),
        'videotec': KeuzelijstWaarde(invulwaarde='videotec',
                                     label='Videotec',
                                     status='ingebruik',
                                     definitie='Videotec',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/videotec')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

