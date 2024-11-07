# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitkraanModelnaam(KeuzelijstField):
    """Modelnamen van afsluitkranen volgens de fabrikant."""
    naam = 'KlAfsluitkraanModelnaam'
    label = 'Modelnaam afsluitkraan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitkraanModelnaam'
    definition = 'Modelnamen van afsluitkranen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitkraanModelnaam'
    options = {
        'e3-gate-valve-dn250': KeuzelijstWaarde(invulwaarde='e3-gate-valve-dn250',
                                                label='E3 gate valve DN250',
                                                status='ingebruik',
                                                definitie='E3 gate valve DN250',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitkraanModelnaam/e3-gate-valve-dn250'),
        'e3-gate-valve-dn50': KeuzelijstWaarde(invulwaarde='e3-gate-valve-dn50',
                                               label='E3 gate valve DN50',
                                               status='ingebruik',
                                               definitie='E3 gate valve DN50',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitkraanModelnaam/e3-gate-valve-dn50')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

