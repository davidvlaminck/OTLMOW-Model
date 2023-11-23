# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRModelnaam(KeuzelijstField):
    """De modelnaam van de ANPR camera."""
    naam = 'KlANPRModelnaam'
    label = 'ANPR modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRModelnaam'
    definition = 'De modelnaam van de ANPR camera.'
    status = 'ingebruik'
    deprecated_version = '2.9.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRModelnaam'
    options = {
        'G1': KeuzelijstWaarde(invulwaarde='G1',
                               label='G1',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G1'),
        'G3': KeuzelijstWaarde(invulwaarde='G3',
                               label='G3',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/G3'),
        'dual': KeuzelijstWaarde(invulwaarde='dual',
                                 label='dual',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/dual'),
        'i-car-cam5': KeuzelijstWaarde(invulwaarde='i-car-cam5',
                                       label='iCar cam5',
                                       status='uitgebruik',
                                       definitie='iCar cam5',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/i-car-cam5'),
        'qcam3': KeuzelijstWaarde(invulwaarde='qcam3',
                                  label='QCAM3',
                                  status='ingebruik',
                                  definitie='QCAM3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/qcam3'),
        'qcam5': KeuzelijstWaarde(invulwaarde='qcam5',
                                  label='QCAM5',
                                  status='ingebruik',
                                  definitie='QCAM5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/qcam5'),
        'vega': KeuzelijstWaarde(invulwaarde='vega',
                                 label='Vega',
                                 status='ingebruik',
                                 definitie='Vega',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRModelnaam/vega')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

