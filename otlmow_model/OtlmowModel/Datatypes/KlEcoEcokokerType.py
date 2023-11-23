# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcokokerType(KeuzelijstField):
    """Types van ecokoker."""
    naam = 'KlEcoEcokokerType'
    label = 'Ecokoker type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcokokerType'
    definition = 'Types van ecokoker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcokokerType'
    options = {
        'amfibieenkoker': KeuzelijstWaarde(invulwaarde='amfibieenkoker',
                                           label='amfibieenkoker',
                                           status='ingebruik',
                                           definitie='Een ecokoker voor amfibieën.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/amfibieenkoker'),
        'betonnen-ecokoker': KeuzelijstWaarde(invulwaarde='betonnen-ecokoker',
                                              label='betonnen ecokoker',
                                              status='ingebruik',
                                              definitie='Een ecokoker uit beton.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcokokerType/betonnen-ecokoker')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

