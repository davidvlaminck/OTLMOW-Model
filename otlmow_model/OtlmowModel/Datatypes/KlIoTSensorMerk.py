# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensorMerk(KeuzelijstField):
    """IoT-senor merken."""
    naam = 'KlIoTSensorMerk'
    label = 'IoT-sensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensorMerk'
    definition = 'IoT-senor merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensorMerk'
    options = {
        'com-sens': KeuzelijstWaarde(invulwaarde='com-sens',
                                     label='COM&SENS',
                                     status='ingebruik',
                                     definitie='COM&SENS',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorMerk/com-sens'),
        'fbgs': KeuzelijstWaarde(invulwaarde='fbgs',
                                 label='FBGS',
                                 status='ingebruik',
                                 definitie='FBGS',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorMerk/fbgs'),
        'leica': KeuzelijstWaarde(invulwaarde='leica',
                                  label='Leica',
                                  status='ingebruik',
                                  definitie='Leica',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorMerk/leica'),
        'rst': KeuzelijstWaarde(invulwaarde='rst',
                                label='RST',
                                status='ingebruik',
                                definitie='RST',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorMerk/rst'),
        'syscom-instruments': KeuzelijstWaarde(invulwaarde='syscom-instruments',
                                               label='SYSCOM Instruments',
                                               status='ingebruik',
                                               definitie='SYSCOM Instruments',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorMerk/syscom-instruments')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

