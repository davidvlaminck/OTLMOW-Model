# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpanningsomvormerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van spanningsomvormers volgens de fabrikant."""
    naam = 'KlSpanningsomvormerModelnaam'
    label = 'Modelnamen spanningsomvormers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpanningsomvormerModelnaam'
    definition = 'Lijst van modelnamen van spanningsomvormers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpanningsomvormerModelnaam'
    options = {
        'minipack': KeuzelijstWaarde(invulwaarde='minipack',
                                     label='Minipack',
                                     status='ingebruik',
                                     definitie='Minipack',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/minipack'),
        'smartpack-s': KeuzelijstWaarde(invulwaarde='smartpack-s',
                                        label='Smartpack S ',
                                        status='ingebruik',
                                        definitie='Smartpack S ',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/smartpack-s')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

