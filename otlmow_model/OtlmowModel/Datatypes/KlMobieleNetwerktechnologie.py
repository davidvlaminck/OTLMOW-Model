# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMobieleNetwerktechnologie(KeuzelijstField):
    """De verschillende generaties van mobiele netwerktechnologieën."""
    naam = 'KlMobieleNetwerktechnologie'
    label = 'Mobiele netwerktechologie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMobieleNetwerktechnologie'
    definition = 'De verschillende generaties van mobiele netwerktechnologieën.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMobieleNetwerktechnologie'
    options = {
        '2g': KeuzelijstWaarde(invulwaarde='2g',
                               label='2G',
                               status='ingebruik',
                               definitie='2G',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMobieleNetwerktechnologie/2g'),
        '3g': KeuzelijstWaarde(invulwaarde='3g',
                               label='3G',
                               status='ingebruik',
                               definitie='3G',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMobieleNetwerktechnologie/3g'),
        '4g': KeuzelijstWaarde(invulwaarde='4g',
                               label='4G',
                               status='ingebruik',
                               definitie='4G',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMobieleNetwerktechnologie/4g'),
        '5g': KeuzelijstWaarde(invulwaarde='5g',
                               label='5G',
                               status='ingebruik',
                               definitie='5G',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMobieleNetwerktechnologie/5g'),
        'vast-netwerk': KeuzelijstWaarde(invulwaarde='vast-netwerk',
                                         label='vast netwerk',
                                         status='ingebruik',
                                         definitie='vast netwerk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMobieleNetwerktechnologie/vast-netwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

