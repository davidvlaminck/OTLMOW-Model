# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeStralingsscherm(KeuzelijstField):
    """Types van stralingsschermen."""
    naam = 'KlTypeStralingsscherm'
    label = 'Type stralingsscherm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeStralingsscherm'
    definition = 'Types van stralingsschermen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeStralingsscherm'
    options = {
        'vaisala-dtr13': KeuzelijstWaarde(invulwaarde='vaisala-dtr13',
                                          label='Vaisala DTR13',
                                          status='ingebruik',
                                          definitie='Vaisala DTR13',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeStralingsscherm/vaisala-dtr13')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

