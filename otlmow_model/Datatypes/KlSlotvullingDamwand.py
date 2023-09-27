# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotvullingDamwand(KeuzelijstField):
    """De vulling van het slot van de damwand."""
    naam = 'KlSlotvullingDamwand'
    label = 'Slotvulling damwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotvullingDamwand'
    definition = 'De vulling van het slot van de damwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotvullingDamwand'
    options = {
        'bitumineuze': KeuzelijstWaarde(invulwaarde='bitumineuze',
                                        label='Bitumineuze',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotvullingDamwand/bitumineuze'),
        'gelaste': KeuzelijstWaarde(invulwaarde='gelaste',
                                    label='Gelaste',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotvullingDamwand/gelaste'),
        'zonder-voegvulling': KeuzelijstWaarde(invulwaarde='zonder-voegvulling',
                                               label='Zonder voegvulling',
                                               status='ingebruik',
                                               definitie='Zonder voegvulling',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotvullingDamwand/zonder-voegvulling'),
        'zwellende': KeuzelijstWaarde(invulwaarde='zwellende',
                                      label='Zwellende',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotvullingDamwand/zwellende')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

