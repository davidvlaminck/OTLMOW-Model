# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPositieKolk(KeuzelijstField):
    """De mogelije posities van een kolk."""
    naam = 'KlPositieKolk'
    label = 'Positie kolk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPositieKolk'
    definition = 'De mogelije posities van een kolk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPositieKolk'
    options = {
        'afwaarts': KeuzelijstWaarde(invulwaarde='afwaarts',
                                     label='afwaarts',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieKolk/afwaarts'),
        'opwaarts': KeuzelijstWaarde(invulwaarde='opwaarts',
                                     label='opwaarts',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieKolk/opwaarts'),
        'slechts-1-kolkdeel': KeuzelijstWaarde(invulwaarde='slechts-1-kolkdeel',
                                               label='slechts 1 kolkdeel',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieKolk/slechts-1-kolkdeel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

