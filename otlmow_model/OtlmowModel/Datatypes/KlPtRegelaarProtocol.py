# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarProtocol(KeuzelijstField):
    """Beschrijft het protocol waarmee de PT-regelaar communiceert."""
    naam = 'KlPtRegelaarProtocol'
    label = 'PT-regelaar protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarProtocol'
    definition = 'Beschrijft het protocol waarmee de PT-regelaar communiceert.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarProtocol'
    options = {
        'R0916': KeuzelijstWaarde(invulwaarde='R0916',
                                  label='R0916',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0916'),
        'R0918': KeuzelijstWaarde(invulwaarde='R0918',
                                  label='R0918',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtRegelaarProtocol/R0918')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

