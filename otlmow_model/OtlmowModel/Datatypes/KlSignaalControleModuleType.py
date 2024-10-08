# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalControleModuleType(KeuzelijstField):
    """Het type van detectie dat uitgevoerd wordt door de signaal controle module."""
    naam = 'KlSignaalControleModuleType'
    label = 'Signaal controle module type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalControleModuleType'
    definition = 'Het type van detectie dat uitgevoerd wordt door de signaal controle module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalControleModuleType'
    options = {
        'kabelbreuk': KeuzelijstWaarde(invulwaarde='kabelbreuk',
                                       label='kabelbreuk',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalControleModuleType/kabelbreuk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

