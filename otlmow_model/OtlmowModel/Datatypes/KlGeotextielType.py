# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGeotextielType(KeuzelijstField):
    """Types van geotextiel."""
    naam = 'KlGeotextielType'
    label = 'Geotextiel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeotextielType'
    definition = 'Types van geotextiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeotextielType'
    options = {
        'anti-vraatdoek': KeuzelijstWaarde(invulwaarde='anti-vraatdoek',
                                           label='anti-vraatdoek',
                                           status='ingebruik',
                                           definitie='anti-vraatdoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/anti-vraatdoek'),
        'bescherming': KeuzelijstWaarde(invulwaarde='bescherming',
                                        label='bescherming',
                                        status='ingebruik',
                                        definitie='bescherming/wapening',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/bescherming'),
        'erosiewerend': KeuzelijstWaarde(invulwaarde='erosiewerend',
                                         label='erosiewerend',
                                         status='ingebruik',
                                         definitie='erosiewerend',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/erosiewerend'),
        'niet-geweven-geotextiel': KeuzelijstWaarde(invulwaarde='niet-geweven-geotextiel',
                                                    label='niet-geweven geotextiel',
                                                    status='ingebruik',
                                                    definitie='niet-geweven geotextiel',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/niet-geweven-geotextiel'),
        'wapening': KeuzelijstWaarde(invulwaarde='wapening',
                                     label='wapening',
                                     status='ingebruik',
                                     definitie='bescherming/wapening',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeotextielType/wapening')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

