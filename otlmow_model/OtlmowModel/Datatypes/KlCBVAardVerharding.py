# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVAardVerharding(KeuzelijstField):
    """Mogelijke waarden voor de aard van de cement/beton verharding."""
    naam = 'KlCBVAardVerharding'
    label = 'CBV aard verharding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVAardVerharding'
    definition = 'Mogelijke waarden voor de aard van de cement/beton verharding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVAardVerharding'
    options = {
        'doorgaand-gewapend-beton': KeuzelijstWaarde(invulwaarde='doorgaand-gewapend-beton',
                                                     label='doorgaand gewapend beton',
                                                     status='ingebruik',
                                                     definitie='Verharding van doorgaand gewapend beton.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/doorgaand-gewapend-beton'),
        'gewapend-beton': KeuzelijstWaarde(invulwaarde='gewapend-beton',
                                           label='gewapend beton',
                                           status='ingebruik',
                                           definitie='Verharding van gewapend beton.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton'),
        'ongewapend-beton': KeuzelijstWaarde(invulwaarde='ongewapend-beton',
                                             label='ongewapend beton',
                                             status='ingebruik',
                                             definitie='Verharding van ongewapend beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton'),
        'staalvezelbeton': KeuzelijstWaarde(invulwaarde='staalvezelbeton',
                                            label='staalvezelbeton',
                                            status='ingebruik',
                                            definitie='Verharding van staalvezelbeton.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

