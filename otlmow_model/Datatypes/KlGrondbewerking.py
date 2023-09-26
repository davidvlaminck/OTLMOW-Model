# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondbewerking(KeuzelijstField):
    """Lijst van mogelijke grondbewerkingen die uitgevoerd kunnen worden."""
    naam = 'KlGrondbewerking'
    label = 'Grondbewerkingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlGrondbewerking'
    definition = 'Lijst van mogelijke grondbewerkingen die uitgevoerd kunnen worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondbewerking'
    options = {
        'diepscheuren': KeuzelijstWaarde(invulwaarde='diepscheuren',
                                         label='diepscheuren',
                                         status='ingebruik',
                                         definitie='Grond voor hergebruik binnen de werfzone.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/diepscheuren'),
        'diepspittengraafmachine': KeuzelijstWaarde(invulwaarde='diepspittengraafmachine',
                                                    label='diepspittenGraafmachine',
                                                    status='ingebruik',
                                                    definitie='Grond voor hergebruik binnen de werfzone.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/diepspittengraafmachine'),
        'egalisereneffenen': KeuzelijstWaarde(invulwaarde='egalisereneffenen',
                                              label='egaliserenEffenen',
                                              status='ingebruik',
                                              definitie='Grond voor hergebruik binnen de werfzone.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/egalisereneffenen'),
        'eggen': KeuzelijstWaarde(invulwaarde='eggen',
                                  label='eggen',
                                  status='ingebruik',
                                  definitie='Grond voor hergebruik binnen de werfzone.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/eggen'),
        'frezen': KeuzelijstWaarde(invulwaarde='frezen',
                                   label='frezen',
                                   status='ingebruik',
                                   definitie='Grond voor hergebruik binnen de werfzone.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/frezen'),
        'ploegen': KeuzelijstWaarde(invulwaarde='ploegen',
                                    label='ploegen',
                                    status='ingebruik',
                                    definitie='Grond voor hergebruik binnen de werfzone.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/ploegen'),
        'rollen': KeuzelijstWaarde(invulwaarde='rollen',
                                   label='rollen',
                                   status='ingebruik',
                                   definitie='Grond voor hergebruik binnen de werfzone.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/rollen'),
        'scheurentriltand': KeuzelijstWaarde(invulwaarde='scheurentriltand',
                                             label='scheurenTriltand',
                                             status='ingebruik',
                                             definitie='Grond voor hergebruik binnen de werfzone.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/scheurentriltand'),
        'scheurenvastetand': KeuzelijstWaarde(invulwaarde='scheurenvastetand',
                                              label='scheurenVasteTand',
                                              status='ingebruik',
                                              definitie='Grond voor hergebruik binnen de werfzone.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/scheurenvastetand'),
        'spitsfrezen': KeuzelijstWaarde(invulwaarde='spitsfrezen',
                                        label='spitsfrezen',
                                        status='ingebruik',
                                        definitie='Grond voor hergebruik binnen de werfzone.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/spitsfrezen'),
        'verkruimelen': KeuzelijstWaarde(invulwaarde='verkruimelen',
                                         label='verkruimelen',
                                         status='ingebruik',
                                         definitie='Grond voor hergebruik binnen de werfzone.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/verkruimelen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

