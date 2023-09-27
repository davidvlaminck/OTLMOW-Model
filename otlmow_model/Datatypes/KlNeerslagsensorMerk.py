# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorMerk(KeuzelijstField):
    """Het merk van de neerslagsensor."""
    naam = 'KlNeerslagsensorMerk'
    label = 'Neerslagsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorMerk'
    definition = 'Het merk van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorMerk'
    options = {
        'Luft': KeuzelijstWaarde(invulwaarde='Luft',
                                 label='Luft',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorMerk/Luft'),
        'dtn': KeuzelijstWaarde(invulwaarde='dtn',
                                label='DTN',
                                status='ingebruik',
                                definitie='DTN',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorMerk/dtn'),
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

