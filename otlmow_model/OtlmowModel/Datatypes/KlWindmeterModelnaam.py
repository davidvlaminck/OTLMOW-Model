# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWindmeterModelnaam(KeuzelijstField):
    """Windmeter modelnamen."""
    naam = 'KlWindmeterModelnaam'
    label = 'Windmeter modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWindmeterModelnaam'
    definition = 'Windmeter modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWindmeterModelnaam'
    options = {
        'wmt700': KeuzelijstWaarde(invulwaarde='wmt700',
                                   label='WMT700',
                                   status='ingebruik',
                                   definitie='WMT700',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterModelnaam/wmt700')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

