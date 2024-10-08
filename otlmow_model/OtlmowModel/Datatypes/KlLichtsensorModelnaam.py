# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtsensorModelnaam(KeuzelijstField):
    """Lichtsensor modelnamen."""
    naam = 'KlLichtsensorModelnaam'
    label = 'Lichtsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtsensorModelnaam'
    definition = 'Lichtsensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtsensorModelnaam'
    options = {
        'luminance-luci-l20': KeuzelijstWaarde(invulwaarde='luminance-luci-l20',
                                               label='Luminance LUCI L20',
                                               status='ingebruik',
                                               definitie='Luminance LUCI L20',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorModelnaam/luminance-luci-l20')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

