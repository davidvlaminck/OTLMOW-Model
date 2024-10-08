# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoutigeType(KeuzelijstField):
    """Types van houtige vegetatie."""
    naam = 'KlHoutigeType'
    label = 'Type houtige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoutigeType'
    definition = 'Types van houtige vegetatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoutigeType'
    options = {
        'bomen---bos': KeuzelijstWaarde(invulwaarde='bomen---bos',
                                        label='bomen - bos',
                                        status='ingebruik',
                                        definitie='Opgaande beplanting van houtachtige gewassen die boomvormend zijn.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/bomen---bos'),
        'houtkant': KeuzelijstWaarde(invulwaarde='houtkant',
                                     label='houtkant',
                                     status='ingebruik',
                                     definitie='Een houtkant is een lijnvormige begroeiing met houtgewas (combinatie van bomen en struiken) met een minimale breedte van 3meter en meer en minstens 1 plantrij. ',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoutigeType/houtkant')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

