# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Detectiecamera."""
    naam = 'KlDetectiecameraMerk'
    label = 'Detectiecamera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraMerk'
    definition = 'Keuzelijst met merknamen voor Detectiecamera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraMerk'
    options = {
        'flir': KeuzelijstWaarde(invulwaarde='flir',
                                 label='FLIR',
                                 status='ingebruik',
                                 definitie='FLIR',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraMerk/flir')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

