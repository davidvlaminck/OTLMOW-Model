# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelType(KeuzelijstField):
    """Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270."""
    naam = 'KlSignaalkabelType'
    label = 'Signalisatiekabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelType'
    definition = 'Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelType'
    options = {
        'coax': KeuzelijstWaarde(invulwaarde='coax',
                                 label='coax',
                                 status='ingebruik',
                                 definitie='coax',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/coax'),
        'coax-rg11': KeuzelijstWaarde(invulwaarde='coax-rg11',
                                      label='coax RG11',
                                      status='ingebruik',
                                      definitie='coax RG11',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/coax-rg11'),
        'coax-rg12': KeuzelijstWaarde(invulwaarde='coax-rg12',
                                      label='coax RG12',
                                      status='ingebruik',
                                      definitie='coax RG12',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/coax-rg12'),
        'coax-rg59': KeuzelijstWaarde(invulwaarde='coax-rg59',
                                      label='coax RG59',
                                      status='ingebruik',
                                      definitie='coax RG59',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/coax-rg59'),
        'elec': KeuzelijstWaarde(invulwaarde='elec',
                                 label='ELEC',
                                 status='ingebruik',
                                 definitie='ELEC',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/elec'),
        'gefaradiseerde-kabel': KeuzelijstWaarde(invulwaarde='gefaradiseerde-kabel',
                                                 label='gefaradiseerde kabel',
                                                 status='ingebruik',
                                                 definitie='gefaradiseerde kabel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/gefaradiseerde-kabel'),
        'koperkabel': KeuzelijstWaarde(invulwaarde='koperkabel',
                                       label='koperkabel',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/koperkabel'),
        'li2ycy': KeuzelijstWaarde(invulwaarde='li2ycy',
                                   label='LI2YCY',
                                   status='ingebruik',
                                   definitie='LI2YCY',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/li2ycy'),
        'liy(st)yy': KeuzelijstWaarde(invulwaarde='liy(st)yy',
                                      label='LiY(st)YY',
                                      status='ingebruik',
                                      definitie='LiY(st)YY',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/liy(st)yy'),
        'liycy': KeuzelijstWaarde(invulwaarde='liycy',
                                  label='LIYCY',
                                  status='ingebruik',
                                  definitie='LIYCY',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/liycy'),
        'liycy(tp)': KeuzelijstWaarde(invulwaarde='liycy(tp)',
                                      label='LIYCY(TP)',
                                      status='ingebruik',
                                      definitie='LIYCY(TP)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/liycy(tp)'),
        'profibuskabel': KeuzelijstWaarde(invulwaarde='profibuskabel',
                                          label='profibuskabel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/profibuskabel'),
        'svab': KeuzelijstWaarde(invulwaarde='svab',
                                 label='SVAB',
                                 status='ingebruik',
                                 definitie='SVAB',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svab'),
        'svavb': KeuzelijstWaarde(invulwaarde='svavb',
                                  label='SVAVB',
                                  status='ingebruik',
                                  definitie='SVAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svavb'),
        'svavb-f2': KeuzelijstWaarde(invulwaarde='svavb-f2',
                                     label='SVAVB-F2',
                                     status='ingebruik',
                                     definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svavb-f2'),
        'svv-f2': KeuzelijstWaarde(invulwaarde='svv-f2',
                                   label='SVV-F2',
                                   status='ingebruik',
                                   definitie='Niet-gewapende signaalkabel voor binnen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svv-f2'),
        'sxag-f2': KeuzelijstWaarde(invulwaarde='sxag-f2',
                                    label='SXAG-F2',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxag-f2'),
        'sxavb': KeuzelijstWaarde(invulwaarde='sxavb',
                                  label='SXAVB',
                                  status='ingebruik',
                                  definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxavb'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  status='ingebruik',
                                  definitie='TWAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/twavb'),
        'xlpe': KeuzelijstWaarde(invulwaarde='xlpe',
                                 label='XLPE',
                                 status='ingebruik',
                                 definitie='XLPE',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/xlpe')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

