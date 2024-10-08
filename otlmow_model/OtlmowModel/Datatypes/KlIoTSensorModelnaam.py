# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensorModelnaam(KeuzelijstField):
    """IoT-sensor modelnamen."""
    naam = 'KlIoTSensorModelnaam'
    label = 'IoT-sensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensorModelnaam'
    definition = 'IoT-sensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensorModelnaam'
    options = {
        'cs-ext': KeuzelijstWaarde(invulwaarde='cs-ext',
                                   label='CS-EXT',
                                   status='ingebruik',
                                   definitie='CS-EXT',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorModelnaam/cs-ext'),
        'ic8161': KeuzelijstWaarde(invulwaarde='ic8161',
                                   label='IC8161',
                                   status='ingebruik',
                                   definitie='IC8161',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorModelnaam/ic8161'),
        'mr3003c': KeuzelijstWaarde(invulwaarde='mr3003c',
                                    label='MR3003C',
                                    status='ingebruik',
                                    definitie='MR3003C',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorModelnaam/mr3003c'),
        'nova-tm60': KeuzelijstWaarde(invulwaarde='nova-tm60',
                                      label='Nova TM60',
                                      status='ingebruik',
                                      definitie='Nova TM60',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorModelnaam/nova-tm60'),
        'tp-01': KeuzelijstWaarde(invulwaarde='tp-01',
                                  label='TP-01',
                                  status='ingebruik',
                                  definitie='TP-01',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorModelnaam/tp-01')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

