# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermbuisKleur(KeuzelijstField):
    """De kleur van de beschermbuis."""
    naam = 'KlBeschermbuisKleur'
    label = 'Beschermbuiskleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisKleur'
    definition = 'De kleur van de beschermbuis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermbuisKleur'
    options = {
        '17': KeuzelijstWaarde(invulwaarde='17',
                               label='17',
                               status='ingebruik',
                               definitie='17',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/17'),
        '28': KeuzelijstWaarde(invulwaarde='28',
                               label='28',
                               status='ingebruik',
                               definitie='28',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/28'),
        'beb': KeuzelijstWaarde(invulwaarde='beb',
                                label='beb',
                                status='ingebruik',
                                definitie='beb',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/beb'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='ingebruik',
                                  definitie='blauw',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/blauw'),
        'blauw-geel': KeuzelijstWaarde(invulwaarde='blauw-geel',
                                       label='blauw-geel',
                                       status='ingebruik',
                                       definitie='blauw-geel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/blauw-geel'),
        'blauw-met-gele-streep': KeuzelijstWaarde(invulwaarde='blauw-met-gele-streep',
                                                  label='blauw-met-gele-streep',
                                                  status='ingebruik',
                                                  definitie='blauw-met-gele-streep',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/blauw-met-gele-streep'),
        'driekleur': KeuzelijstWaarde(invulwaarde='driekleur',
                                      label='driekleur',
                                      status='ingebruik',
                                      definitie='driekleur',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/driekleur'),
        'geel': KeuzelijstWaarde(invulwaarde='geel',
                                 label='geel',
                                 status='ingebruik',
                                 definitie='geel',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/geel'),
        'glasvezelbuis': KeuzelijstWaarde(invulwaarde='glasvezelbuis',
                                          label='glasvezelbuis',
                                          status='ingebruik',
                                          definitie='glasvezelbuis',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/glasvezelbuis'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='ingebruik',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/grijs'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='groen',
                                  status='ingebruik',
                                  definitie='groen',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/groen'),
        'multi': KeuzelijstWaarde(invulwaarde='multi',
                                  label='multi',
                                  status='ingebruik',
                                  definitie='multi',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/multi'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     status='ingebruik',
                                     definitie='onbekend',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/onbekend'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   status='ingebruik',
                                   definitie='oranje',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/oranje'),
        'patchkoord': KeuzelijstWaarde(invulwaarde='patchkoord',
                                       label='patchkoord',
                                       status='ingebruik',
                                       definitie='patchkoord',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/patchkoord'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/rood'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                definitie='rvs',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/rvs'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='ingebruik',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/zwart'),
        'zwart-met-groene-streep': KeuzelijstWaarde(invulwaarde='zwart-met-groene-streep',
                                                    label='zwart-met-groene-streep',
                                                    status='ingebruik',
                                                    definitie='zwart-met-groene-streep',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisKleur/zwart-met-groene-streep')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

