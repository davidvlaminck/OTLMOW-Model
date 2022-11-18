# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoppinzuilType(KeuzelijstField):
    """De types van een analoge hoppinzuil."""
    naam = 'KlHoppinzuilType'
    label = 'Hoppinzuil type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoppinzuilType'
    definition = 'De types van een analoge hoppinzuil.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoppinzuilType'
    options = {
        'analoog-groot': KeuzelijstWaarde(invulwaarde='analoog-groot',
                                          label='Analoog groot',
                                          status='ingebruik',
                                          definitie='Hoppinzuil met een minimale afmeting van 55x10x280 cm waarop de veranderlijke informatie analoog (op papier/sticker) wordt weergegeven.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoppinzuilType/analoog-groot'),
        'analoog-mini': KeuzelijstWaarde(invulwaarde='analoog-mini',
                                         label='Analoog mini',
                                         status='ingebruik',
                                         definitie='Hoppinzuil met een minimale afmeting van 40x3x200 cm waarop de veranderlijke informatie analoog (op papier/sticker) wordt weergegeven.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoppinzuilType/analoog-mini')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

