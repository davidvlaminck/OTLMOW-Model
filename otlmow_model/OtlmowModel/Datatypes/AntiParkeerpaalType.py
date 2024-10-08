# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class AntiParkeerpaalType(KeuzelijstField):
    """De vormen van een anti-parkeerpaal."""
    naam = 'AntiParkeerpaalType'
    label = 'Anti-parkeerpaal type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AntiParkeerpaalType'
    definition = 'De vormen van een anti-parkeerpaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/AntiParkeerpaalType'
    options = {
        'conischeTrottoirpaalAmsterdammer': KeuzelijstWaarde(invulwaarde='conischeTrottoirpaalAmsterdammer',
                                                             label='conischeTrottoirpaalAmsterdammer',
                                                             status='ingebruik',
                                                             definitie='Conische paal met afgeronde kop en sierring.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/conischeTrottoirpaalAmsterdammer'),
        'diamantkoppaal': KeuzelijstWaarde(invulwaarde='diamantkoppaal',
                                           label='diamantkoppaal',
                                           status='ingebruik',
                                           definitie='Een paal voorzien van een diamantkop en op de hoeken 4 vellingkanten.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/AntiParkeerpaalType/diamantkoppaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

