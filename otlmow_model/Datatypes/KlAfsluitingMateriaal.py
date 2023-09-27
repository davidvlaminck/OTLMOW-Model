# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitingMateriaal(KeuzelijstField):
    """Het materiaal waaruit de afsluiting vervaardigd is."""
    naam = 'KlAfsluitingMateriaal'
    label = 'Afsluiting materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitingMateriaal'
    definition = 'Het materiaal waaruit de afsluiting vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitingMateriaal'
    options = {
        'geplastificeerde-metaaldraad': KeuzelijstWaarde(invulwaarde='geplastificeerde-metaaldraad',
                                                         label='(Geplastificeerde) Metaaldraad',
                                                         status='ingebruik',
                                                         definitie='(Geplastificeerde) Metaaldraad',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitingMateriaal/geplastificeerde-metaaldraad'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='Metaal',
                                   status='ingebruik',
                                   definitie='Metaal',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluitingMateriaal/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

