# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        'acti': KeuzelijstWaarde(invulwaarde='acti',
                                 label='ACTi',
                                 status='ingebruik',
                                 definitie='ACTi',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/acti'),
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
        'macq': KeuzelijstWaarde(invulwaarde='macq',
                                 label='Macq',
                                 status='ingebruik',
                                 definitie='Macq',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/macq'),
        'mobotix': KeuzelijstWaarde(invulwaarde='mobotix',
                                    label='Mobotix',
                                    status='ingebruik',
                                    definitie='Mobotix',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/mobotix'),
        'pelco': KeuzelijstWaarde(invulwaarde='pelco',
                                  label='Pelco',
                                  status='ingebruik',
                                  definitie='Pelco',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/pelco'),
        'tatille': KeuzelijstWaarde(invulwaarde='tatille',
                                    label='Tatille',
                                    status='ingebruik',
                                    definitie='Tatille',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraMerk/tatille'),
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

