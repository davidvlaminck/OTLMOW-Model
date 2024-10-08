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
                                           status='uitgebruik',
                                           definitie='Verharding van gewapend beton.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton'),
        'gewapend-beton-met-deuvels': KeuzelijstWaarde(invulwaarde='gewapend-beton-met-deuvels',
                                                       label='gewapend beton met deuvels',
                                                       status='ingebruik',
                                                       definitie='Verharding van gewapend beton met deuvels.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton-met-deuvels'),
        'gewapend-beton-zonder-deuvels': KeuzelijstWaarde(invulwaarde='gewapend-beton-zonder-deuvels',
                                                          label='gewapend beton zonder deuvels',
                                                          status='ingebruik',
                                                          definitie='Verharding van gewapend beton zonder deuvels',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/gewapend-beton-zonder-deuvels'),
        'ongewapend-beton': KeuzelijstWaarde(invulwaarde='ongewapend-beton',
                                             label='ongewapend beton',
                                             status='uitgebruik',
                                             definitie='Verharding van ongewapend beton.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton'),
        'ongewapend-beton-met-deuvels': KeuzelijstWaarde(invulwaarde='ongewapend-beton-met-deuvels',
                                                         label='ongewapend beton met deuvels',
                                                         status='ingebruik',
                                                         definitie='Verharding van ongewapend beton met deuvels.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton-met-deuvels'),
        'ongewapend-beton-zonder-deuvels': KeuzelijstWaarde(invulwaarde='ongewapend-beton-zonder-deuvels',
                                                            label='ongewapend beton zonder deuvels',
                                                            status='ingebruik',
                                                            definitie='Verharding van ongewapend beton zonder deuvels.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/ongewapend-beton-zonder-deuvels'),
        'staalvezelbeton': KeuzelijstWaarde(invulwaarde='staalvezelbeton',
                                            label='staalvezelbeton',
                                            status='uitgebruik',
                                            definitie='Verharding van staalvezelbeton.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton'),
        'staalvezelbeton-met-deuvels': KeuzelijstWaarde(invulwaarde='staalvezelbeton-met-deuvels',
                                                        label='staalvezelbeton met deuvels',
                                                        status='ingebruik',
                                                        definitie='Verharding van staalvezelbeton met deuvels.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton-met-deuvels'),
        'staalvezelbeton-zonder-deuvels': KeuzelijstWaarde(invulwaarde='staalvezelbeton-zonder-deuvels',
                                                           label='staalvezelbeton zonder deuvels',
                                                           status='ingebruik',
                                                           definitie='Verharding van staalvezelbeton zonder deuvels.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVAardVerharding/staalvezelbeton-zonder-deuvels')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

