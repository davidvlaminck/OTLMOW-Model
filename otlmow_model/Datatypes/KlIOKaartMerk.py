# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOKaartMerk(KeuzelijstField):
    """Lijst van mogelijke merken voor IO-kaarten."""
    naam = 'KlIOKaartMerk'
    label = 'IO-kaart merken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOKaartMerk'
    definition = 'Lijst van mogelijke merken voor IO-kaarten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOKaartMerk'
    options = {
        'dtn': KeuzelijstWaarde(invulwaarde='dtn',
                                label='DTN',
                                status='ingebruik',
                                definitie='DTN',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartMerk/dtn'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartMerk/phoenix-contact'),
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

