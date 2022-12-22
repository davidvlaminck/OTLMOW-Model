# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitgravingSoorten(KeuzelijstField):
    """De specificatie van type grond bij uitgraving."""
    naam = 'KlUitgravingSoorten'
    label = 'Uitgraving soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlUitgravingSoorten'
    definition = 'De specificatie van type grond bij uitgraving.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitgravingSoorten'
    options = {
        'compacte-grond': KeuzelijstWaarde(invulwaarde='compacte-grond',
                                           label='compacte grond',
                                           status='ingebruik',
                                           definitie='Uitgraving in compacte grond.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitgravingSoorten/compacte-grond'),
        'losse-grond': KeuzelijstWaarde(invulwaarde='losse-grond',
                                        label='losse grond',
                                        status='ingebruik',
                                        definitie='Uitgraving van losse grond.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitgravingSoorten/losse-grond'),
        'plaatselijke-uitvoering': KeuzelijstWaarde(invulwaarde='plaatselijke-uitvoering',
                                                    label='plaatselijke uitvoering',
                                                    status='ingebruik',
                                                    definitie='De uitgraving van grond in functie van plaatselijke uitvoering.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitgravingSoorten/plaatselijke-uitvoering'),
        'rotsachtige-grond': KeuzelijstWaarde(invulwaarde='rotsachtige-grond',
                                              label='rotsachtige grond',
                                              status='ingebruik',
                                              definitie='Uitgraving in rotsachtige grond.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitgravingSoorten/rotsachtige-grond')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

