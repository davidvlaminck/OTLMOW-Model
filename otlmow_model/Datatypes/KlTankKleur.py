# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankKleur(KeuzelijstField):
    """De kleur van de tank."""
    naam = 'KlTankKleur'
    label = 'Tank kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankKleur'
    definition = 'De kleur van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankKleur'
    options = {
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='Blauw',
                                  status='ingebruik',
                                  definitie='Blauw',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/blauw'),
        'bruin': KeuzelijstWaarde(invulwaarde='bruin',
                                  label='Bruin',
                                  status='ingebruik',
                                  definitie='Bruin',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/bruin'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='Grijs',
                                  status='ingebruik',
                                  definitie='Grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/grijs'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='Groen',
                                  status='ingebruik',
                                  definitie='Groen',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/groen'),
        'paars': KeuzelijstWaarde(invulwaarde='paars',
                                  label='Paars',
                                  status='ingebruik',
                                  definitie='Paars',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/paars'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='Rood',
                                 status='ingebruik',
                                 definitie='Rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='Wit',
                                status='ingebruik',
                                definitie='Wit',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/wit'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='Zwart',
                                  status='ingebruik',
                                  definitie='Zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankKleur/zwart')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

