# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlThermoHygrometerMerk(KeuzelijstField):
    """Thermo- hygrometer merken."""
    naam = 'KlThermoHygrometerMerk'
    label = 'Thermo- hygrometer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlThermoHygrometerMerk'
    definition = 'Thermo- hygrometer merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlThermoHygrometerMerk'
    options = {
        'apc': KeuzelijstWaarde(invulwaarde='apc',
                                label='APC',
                                status='ingebruik',
                                definitie='APC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerMerk/apc'),
        'gude': KeuzelijstWaarde(invulwaarde='gude',
                                 label='Gude',
                                 status='ingebruik',
                                 definitie='Gude',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerMerk/gude'),
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlThermoHygrometerMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

