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
        'hmp155': KeuzelijstWaarde(invulwaarde='hmp155',
                                   label='HMP155',
                                   status='ingebruik',
                                   definitie='HMP155',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerModelnaam/hmp155')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

