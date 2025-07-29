# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPyranometerMerk(KeuzelijstField):
    """Pyranometer merken."""
    naam = 'KlPyranometerMerk'
    label = 'Pyranometer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPyranometerMerk'
    definition = 'Pyranometer merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPyranometerMerk'
    options = {
        'kipp-zonen': KeuzelijstWaarde(invulwaarde='kipp-zonen',
                                       label='Kipp & Zonen',
                                       status='ingebruik',
                                       definitie='Kipp & Zonen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPyranometerMerk/kipp-zonen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

