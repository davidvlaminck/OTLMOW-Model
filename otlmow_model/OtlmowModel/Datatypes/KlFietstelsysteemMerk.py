# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFietstelsysteemMerk(KeuzelijstField):
    """Lijst van mogelijke merknamen voor fietstelsystemen."""
    naam = 'KlFietstelsysteemMerk'
    label = 'Merknaam fietstelsysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFietstelsysteemMerk'
    definition = 'Lijst van mogelijke merknamen voor fietstelsystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFietstelsysteemMerk'
    options = {
        'eco-counter': KeuzelijstWaarde(invulwaarde='eco-counter',
                                        label='eco-counter',
                                        status='ingebruik',
                                        definitie='eco-counter',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFietstelsysteemMerk/eco-counter')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

