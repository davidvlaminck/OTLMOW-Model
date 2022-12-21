# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElektromotorBeschermingsgraad(KeuzelijstField):
    """De beschmeringsgraad van een elektromotor, uitgerdukt als 'IP', gevolgd door 2 cijfers."""
    naam = 'KlElektromotorBeschermingsgraad'
    label = 'Elektromotor beschermingsgraad'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElektromotorBeschermingsgraad'
    definition = "De beschmeringsgraad van een elektromotor, uitgerdukt als 'IP', gevolgd door 2 cijfers."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElektromotorBeschermingsgraad'
    options = {
        'ip20': KeuzelijstWaarde(invulwaarde='ip20',
                                 label='IP20',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBeschermingsgraad/ip20')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

