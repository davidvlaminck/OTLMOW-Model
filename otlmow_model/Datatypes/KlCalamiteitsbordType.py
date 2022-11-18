# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordType(KeuzelijstField):
    """Types van calamiteitsbord."""
    naam = 'KlCalamiteitsbordType'
    label = 'Calamiteitsbord type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordType'
    definition = 'Types van calamiteitsbord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordType'
    options = {
        'draaiend-bord': KeuzelijstWaarde(invulwaarde='draaiend-bord',
                                          label='draaiend bord',
                                          status='ingebruik',
                                          definitie='Een draaiend calamiteitsbord.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/draaiend-bord'),
        'dragend-bord': KeuzelijstWaarde(invulwaarde='dragend-bord',
                                         label='dragend bord',
                                         status='ingebruik',
                                         definitie='Een dragend calamiteitsbord.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/dragend-bord')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

