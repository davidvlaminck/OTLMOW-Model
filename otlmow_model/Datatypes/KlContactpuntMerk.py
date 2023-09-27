# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntMerk(KeuzelijstField):
    """Lijst van merknamen van contactpunten volgens de fabrikant."""
    naam = 'KlContactpuntMerk'
    label = 'Merknamen contactpunten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntMerk'
    definition = 'Lijst van merknamen van contactpunten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntMerk'
    options = {
        'heinen': KeuzelijstWaarde(invulwaarde='heinen',
                                   label='Heinen',
                                   status='ingebruik',
                                   definitie='Heinen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntMerk/heinen'),
        'locinox': KeuzelijstWaarde(invulwaarde='locinox',
                                    label='LOCINOX',
                                    status='ingebruik',
                                    definitie='LOCINOX',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntMerk/locinox')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

