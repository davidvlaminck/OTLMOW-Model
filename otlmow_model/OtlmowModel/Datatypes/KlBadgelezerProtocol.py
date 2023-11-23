# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBadgelezerProtocol(KeuzelijstField):
    """Lijst van protocollen gebruikt door badgelezers."""
    naam = 'KlBadgelezerProtocol'
    label = 'Badgelezer protocollen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBadgelezerProtocol'
    definition = 'Lijst van protocollen gebruikt door badgelezers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBadgelezerProtocol'
    options = {
        'rs485': KeuzelijstWaarde(invulwaarde='rs485',
                                  label='RS485',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBadgelezerProtocol/rs485')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

