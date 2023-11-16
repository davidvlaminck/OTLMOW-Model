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
                                         definitie='Het breken van de ondergrond met een machine met scheurtanden waarvan de tussenafstand maximaal 0,60 m bedraagt. Het breken gebeurt tot op een diepte van 0,60 m, tenzij anders vermeld in de opdrachtdocumenten.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/diepscheuren'),
        'diepspittengraafmachine': KeuzelijstWaarde(invulwaarde='diepspittengraafmachine',
                                                    label='diepspittenGraafmachine',
                                                    status='ingebruik',
                                                    definitie='Het met de graafmachine en gebruik van aangepaste graafbak losmaken van de grond tot op 0,50 m diepte, tenzij anders vermeld in de opdrachtdocumenten.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/diepspittengraafmachine'),
        'egalisereneffenen': KeuzelijstWaarde(invulwaarde='egalisereneffenen',
                                              label='egaliserenEffenen',
                                              status='ingebruik',
                                              definitie='Het egaliseren of effenen van de grond met een egalisatiemachine tot een vlak grondoppervlak verkregen wordt.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/egalisereneffenen'),
        'eggen': KeuzelijstWaarde(invulwaarde='eggen',
                                  label='eggen',
                                  status='ingebruik',
                                  definitie='Het door middel van een getrokken eg verkruimelen van de bovenste laag van de bewerkte grond tot op een diepte van 0,10 m.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/eggen'),
        'frezen': KeuzelijstWaarde(invulwaarde='frezen',
                                   label='frezen',
                                   status='ingebruik',
                                   definitie='Het met een roterende frees breken en mengen van de ondergrond tot op een diepte van 0,20 m.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/frezen'),
        'ploegen': KeuzelijstWaarde(invulwaarde='ploegen',
                                    label='ploegen',
                                    status='ingebruik',
                                    definitie='Het met de ploeg keren van de grond waarbij de zode tot een diepte van minimaal 0,30 m in de niet bewerkte grond wordt ondergewerkt.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/ploegen'),
        'rollen': KeuzelijstWaarde(invulwaarde='rollen',
                                   label='rollen',
                                   status='ingebruik',
                                   definitie='Het aandrukken van de grond door middel van een getrokken gladde rol met een gewicht van 150 kg per lopende meter velgbreedte.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/rollen'),
        'scheurentriltand': KeuzelijstWaarde(invulwaarde='scheurentriltand',
                                             label='scheurenTriltand',
                                             status='ingebruik',
                                             definitie='Het met de triltandcultivator met smalle tanden loswoelen van de grond tot op een diepte van 0,20 m in de niet bewerkte grond.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/scheurentriltand'),
        'scheurenvastetand': KeuzelijstWaarde(invulwaarde='scheurenvastetand',
                                              label='scheurenVasteTand',
                                              status='ingebruik',
                                              definitie='Het met een vastetandcultivator met smalle tanden, geplaatst op 2 rijen in verband, loswoelen van de grond tot op een diepte van 0,40 m, tenzij anders vermeld in de opdrachtdocumenten.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/scheurenvastetand'),
        'spitsfrezen': KeuzelijstWaarde(invulwaarde='spitsfrezen',
                                        label='spitsfrezen',
                                        status='ingebruik',
                                        definitie='Het met een spitmachine met roterende tanden breken van de grond tot op een diepte van 0,30 m in de niet bewerkte grond.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/spitsfrezen'),
        'verkruimelen': KeuzelijstWaarde(invulwaarde='verkruimelen',
                                         label='verkruimelen',
                                         status='ingebruik',
                                         definitie='Het door middel van een ronde veer of (kooi)rol verkruimelen van de bovenste laag van de bewerkte grond tot op een diepte van 0,05 m tot wanneer een vlakke en fijne ondergrond wordt verkregen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondbewerking/verkruimelen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

