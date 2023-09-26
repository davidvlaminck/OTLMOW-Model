# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomtoestandMeerwaardefactor(KeuzelijstField):
    """De meerwaarde (ecologisch,erfgoed) van de boom."""
    naam = 'KlBoomtoestandMeerwaardefactor'
    label = 'Boomtoestand meerwaardefactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomtoestandMeerwaardefactor'
    definition = 'De meerwaarde (ecologisch,erfgoed) van de boom.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomtoestandMeerwaardefactor'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/1'),
        '15': KeuzelijstWaarde(invulwaarde='15',
                               label='15',
                               status='ingebruik',
                               definitie='15',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/15'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/2'),
        '25': KeuzelijstWaarde(invulwaarde='25',
                               label='25',
                               status='ingebruik',
                               definitie='25',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/25')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

