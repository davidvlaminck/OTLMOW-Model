# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBemesting(KeuzelijstField):
    """Het toevoegen van en verwerken van meststoffen zowel bij aanleg alsook bij beheer."""
    naam = 'KlBemesting'
    label = 'Bemesting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBemesting'
    definition = 'Het toevoegen van en verwerken van meststoffen zowel bij aanleg alsook bij beheer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBemesting'
    options = {
        'meststoffen': KeuzelijstWaarde(invulwaarde='meststoffen',
                                        label='meststoffen',
                                        status='ingebruik',
                                        definitie='Grond voor hergebruik binnen de werfzone.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBemesting/meststoffen'),
        'meststoftabletten': KeuzelijstWaarde(invulwaarde='meststoftabletten',
                                              label='meststoftabletten',
                                              status='ingebruik',
                                              definitie='Grond voor hergebruik binnen de werfzone.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBemesting/meststoftabletten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

