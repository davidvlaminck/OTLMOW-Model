# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlThermoHygrometerModelnaam(KeuzelijstField):
    """Thermo- hygrometer modelnamen."""
    naam = 'KlThermoHygrometerModelnaam'
    label = 'Thermo- hygrometer modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlThermoHygrometerModelnaam'
    definition = 'Thermo- hygrometer modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlThermoHygrometerModelnaam'
    options = {
        'ap9319': KeuzelijstWaarde(invulwaarde='ap9319',
                                   label='AP9319',
                                   status='ingebruik',
                                   definitie='AP9319',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/ap9319'),
        'expert-sensor-box-7213-1': KeuzelijstWaarde(invulwaarde='expert-sensor-box-7213-1',
                                                     label='Expert Sensor Box 7213-1',
                                                     status='ingebruik',
                                                     definitie='Expert Sensor Box 7213-1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/expert-sensor-box-7213-1'),
        'expert-sensor-box-7213-2': KeuzelijstWaarde(invulwaarde='expert-sensor-box-7213-2',
                                                     label=' Expert Sensor Box 7213-2',
                                                     status='ingebruik',
                                                     definitie=' Expert Sensor Box 7213-2',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/expert-sensor-box-7213-2'),
        'hmp155': KeuzelijstWaarde(invulwaarde='hmp155',
                                   label='HMP155',
                                   status='ingebruik',
                                   definitie='HMP155',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/hmp155'),
        'nbrk0200': KeuzelijstWaarde(invulwaarde='nbrk0200',
                                     label='NBRK0200',
                                     status='ingebruik',
                                     definitie='NBRK0200',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/nbrk0200'),
        'nbrk0250': KeuzelijstWaarde(invulwaarde='nbrk0250',
                                     label='NBRK0250',
                                     status='ingebruik',
                                     definitie='NBRK0250',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/nbrk0250')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

