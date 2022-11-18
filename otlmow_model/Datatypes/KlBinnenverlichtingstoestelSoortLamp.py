# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSoortLamp(KeuzelijstField):
    """Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen."""
    naam = 'KlBinnenverlichtingstoestelSoortLamp'
    label = 'Binnenverlichtingstoestel soort lamp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSoortLamp'
    definition = 'Lijst van mogelijke soorten lampen voor binnenverlichtingstoestellen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSoortLamp'
    options = {
        'LED': KeuzelijstWaarde(invulwaarde='LED',
                                label='LED',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/LED'),
        'TL': KeuzelijstWaarde(invulwaarde='TL',
                               label='TL',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/TL'),
        'gloeilamp': KeuzelijstWaarde(invulwaarde='gloeilamp',
                                      label='gloeilamp',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/gloeilamp'),
        'halogeen': KeuzelijstWaarde(invulwaarde='halogeen',
                                     label='halogeen',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/halogeen'),
        'spaarlamp': KeuzelijstWaarde(invulwaarde='spaarlamp',
                                      label='spaarlamp',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSoortLamp/spaarlamp')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

