# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgFaalmodusType(KeuzelijstField):
    """Keuzelijst voor de types failure modes van een beveiligingssysteem."""
    naam = 'KlAlgFaalmodusType'
    label = 'Algemeen faalmodus type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgFaalmodusType'
    definition = 'Keuzelijst voor de types failure modes van een beveiligingssysteem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgFaalmodusType'
    options = {
        'fail-safe': KeuzelijstWaarde(invulwaarde='fail-safe',
                                      label='fail safe',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgFaalmodusType/fail-safe'),
        'fail-secure': KeuzelijstWaarde(invulwaarde='fail-secure',
                                        label='fail secure',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgFaalmodusType/fail-secure')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

