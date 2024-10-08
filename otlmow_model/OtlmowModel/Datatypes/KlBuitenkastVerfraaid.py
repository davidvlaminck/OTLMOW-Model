# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBuitenkastVerfraaid(KeuzelijstField):
    """Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund."""
    naam = 'KlBuitenkastVerfraaid'
    label = 'Verfraaiing buitenkast'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlBuitenkastVerfraaid'
    definition = 'Mogelijke types voor verfraaiing als combinatie van aan- en afwezigheid en al dan niet vegund.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBuitenkastVerfraaid'
    options = {
        'ja': KeuzelijstWaarde(invulwaarde='ja',
                               label='ja',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja'),
        'ja-niet-vergund': KeuzelijstWaarde(invulwaarde='ja-niet-vergund',
                                            label='ja niet vergund',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/ja-niet-vergund'),
        'nee': KeuzelijstWaarde(invulwaarde='nee',
                                label='nee',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBuitenkastVerfraaid/nee')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

