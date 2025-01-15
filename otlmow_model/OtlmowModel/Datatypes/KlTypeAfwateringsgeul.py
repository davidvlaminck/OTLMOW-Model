# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeAfwateringsgeul(KeuzelijstField):
    """De mogelijke types van een afwateringsgeul."""
    naam = 'KlTypeAfwateringsgeul'
    label = 'type afwateringsgeul'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeAfwateringsgeul'
    definition = 'De mogelijke types van een afwateringsgeul.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeAfwateringsgeul'
    options = {
        'roostergoot': KeuzelijstWaarde(invulwaarde='roostergoot',
                                        label='roostergoot',
                                        status='ingebruik',
                                        definitie=' Een afwateringsgeul afgedekt met een rooster.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAfwateringsgeul/roostergoot'),
        'verholen-goot': KeuzelijstWaarde(invulwaarde='verholen-goot',
                                          label='verholen goot',
                                          status='ingebruik',
                                          definitie='Een afwateringsgeul uitgerust met een  sleufvormige inlaatopening.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAfwateringsgeul/verholen-goot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

