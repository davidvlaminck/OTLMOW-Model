# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlANPRMerk(KeuzelijstField):
    """Het merk van de ANPR-camera."""
    naam = 'KlANPRMerk'
    label = 'ANPR-camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlANPRMerk'
    definition = 'Het merk van de ANPR-camera.'
    status = 'ingebruik'
    deprecated_version = '2.9.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlANPRMerk'
    options = {
        'Macq': KeuzelijstWaarde(invulwaarde='Macq',
                                 label='Macq',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Macq'),
        'Tattile': KeuzelijstWaarde(invulwaarde='Tattile',
                                    label='Tattile',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlANPRMerk/Tattile')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

