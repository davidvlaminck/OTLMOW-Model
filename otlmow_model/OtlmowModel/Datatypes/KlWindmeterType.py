# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWindmeterType(KeuzelijstField):
    """Types van windmeters."""
    naam = 'KlWindmeterType'
    label = 'Windmeter type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWindmeterType'
    definition = 'Types van windmeters.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWindmeterType'
    options = {
        'ultrasoon': KeuzelijstWaarde(invulwaarde='ultrasoon',
                                      label='Ultrasoon',
                                      status='ingebruik',
                                      definitie='Ultrasoon',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterType/ultrasoon')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

