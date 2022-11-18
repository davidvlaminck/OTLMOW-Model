# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSchachtHeipaal(KeuzelijstField):
    """Het type van de schacht van de heipaal."""
    naam = 'KlTypeSchachtHeipaal'
    label = 'Type schacht van de heipaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSchachtHeipaal'
    definition = 'Het type van de schacht van de heipaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSchachtHeipaal'
    options = {
        'aardvochtig-gestampt-beton': KeuzelijstWaarde(invulwaarde='aardvochtig-gestampt-beton',
                                                       label='Aardvochtig gestampt beton',
                                                       status='ingebruik',
                                                       definitie='De schacht is opgevuld met aardvochtig gestampt beton.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchachtHeipaal/aardvochtig-gestampt-beton'),
        'geen-schacht': KeuzelijstWaarde(invulwaarde='geen-schacht',
                                         label='Geen schacht',
                                         status='ingebruik',
                                         definitie='De heipaal heeft geen schacht.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchachtHeipaal/geen-schacht'),
        'plastisch-beton': KeuzelijstWaarde(invulwaarde='plastisch-beton',
                                            label='Plastisch beton',
                                            status='ingebruik',
                                            definitie='De schacht is opgevuld met plastisch beton.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchachtHeipaal/plastisch-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

