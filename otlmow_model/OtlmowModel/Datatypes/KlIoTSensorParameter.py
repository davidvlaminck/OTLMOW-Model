# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensorParameter(KeuzelijstField):
    """IoT-sensor parameters."""
    naam = 'KlIoTSensorParameter'
    label = 'IoT-sensor parameter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensorParameter'
    definition = 'IoT-sensor parameters.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensorParameter'
    options = {
        'hoekverdraaiing': KeuzelijstWaarde(invulwaarde='hoekverdraaiing',
                                            label='Hoekverdraaiing',
                                            status='ingebruik',
                                            definitie='Hoekverdraaiing',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/hoekverdraaiing'),
        'rek': KeuzelijstWaarde(invulwaarde='rek',
                                label='Rek',
                                status='ingebruik',
                                definitie='Rek',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/rek'),
        'temperatuur': KeuzelijstWaarde(invulwaarde='temperatuur',
                                        label='Temperatuur',
                                        status='ingebruik',
                                        definitie='Temperatuur',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/temperatuur'),
        'trillingen': KeuzelijstWaarde(invulwaarde='trillingen',
                                       label='Trillingen',
                                       status='ingebruik',
                                       definitie='Trillingen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/trillingen'),
        'verplaatsing': KeuzelijstWaarde(invulwaarde='verplaatsing',
                                         label='Verplaatsing',
                                         status='ingebruik',
                                         definitie='Verplaatsing',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/verplaatsing'),
        'vibraties': KeuzelijstWaarde(invulwaarde='vibraties',
                                      label='Vibraties',
                                      status='verwijderd',
                                      definitie='Vibraties',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/vibraties'),
        'vibraties-of-trillingen': KeuzelijstWaarde(invulwaarde='vibraties-of-trillingen',
                                                    label='Vibraties of trillingen',
                                                    status='verwijderd',
                                                    definitie='Vibraties of trillingen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorParameter/vibraties-of-trillingen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

