# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeHanger(KeuzelijstField):
    """Het type hanger"""
    naam = 'KlTypeHanger'
    label = 'Type hanger'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeHanger'
    definition = 'Het type hanger'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeHanger'
    options = {
        'kabel': KeuzelijstWaarde(invulwaarde='kabel',
                                  label='kabel',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHanger/kabel'),
        'staaf': KeuzelijstWaarde(invulwaarde='staaf',
                                  label='staaf',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHanger/staaf')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

