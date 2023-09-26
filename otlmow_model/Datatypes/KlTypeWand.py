# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWand(KeuzelijstField):
    """De functie die de wand uitoefent."""
    naam = 'KlTypeWand'
    label = 'Type wand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeWand'
    definition = 'De functie die de wand uitoefent.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWand'
    options = {
        'binnenwand': KeuzelijstWaarde(invulwaarde='binnenwand',
                                       label='binnenwand',
                                       status='ingebruik',
                                       definitie='Wand zonder dragende functie, meestal gebruikt om ruimtes van elkaar te scheiden.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/binnenwand'),
        'brilwand': KeuzelijstWaarde(invulwaarde='brilwand',
                                     label='brilwand',
                                     status='ingebruik',
                                     definitie='Wand met een uitsparing/opening voor het doorlaten van een tunnelboormachine.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/brilwand'),
        'steunwand': KeuzelijstWaarde(invulwaarde='steunwand',
                                      label='steunwand',
                                      status='ingebruik',
                                      definitie='Wand die ontworpen is om belastingen te dragen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/steunwand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

