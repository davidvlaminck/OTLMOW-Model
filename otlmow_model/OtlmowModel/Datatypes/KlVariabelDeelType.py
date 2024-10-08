# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVariabelDeelType(KeuzelijstField):
    """Types van het variabel deel van een overstortrand."""
    naam = 'KlVariabelDeelType'
    label = 'Variabel deel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVariabelDeelType'
    definition = 'Types van het variabel deel van een overstortrand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVariabelDeelType'
    options = {
        'overstortplaat': KeuzelijstWaarde(invulwaarde='overstortplaat',
                                           label='overstortplaat',
                                           status='ingebruik',
                                           definitie='overstortplaat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/overstortplaat'),
        'schotbalk': KeuzelijstWaarde(invulwaarde='schotbalk',
                                      label='schotbalk',
                                      status='ingebruik',
                                      definitie='schotbalk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVariabelDeelType/schotbalk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

