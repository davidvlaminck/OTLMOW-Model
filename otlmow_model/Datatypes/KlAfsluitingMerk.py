# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitingMerk(KeuzelijstField):
    """Het merk van een afsluiting."""
    naam = 'KlAfsluitingMerk'
    label = 'Afsluiting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitingMerk'
    definition = 'Het merk van een afsluiting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitingMerk'
    options = {
        'bekaert': KeuzelijstWaarde(invulwaarde='bekaert',
                                    label='Bekaert',
                                    status='ingebruik',
                                    definitie='Bekaert',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitingMerk/bekaert'),
        'hilfra': KeuzelijstWaarde(invulwaarde='hilfra',
                                   label='Hilfra',
                                   status='ingebruik',
                                   definitie='Hilfra',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitingMerk/hilfra'),
        'horta': KeuzelijstWaarde(invulwaarde='horta',
                                  label='Horta',
                                  status='ingebruik',
                                  definitie='Horta',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitingMerk/horta')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

