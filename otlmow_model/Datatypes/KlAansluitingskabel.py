# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitingskabel(KeuzelijstField):
    """Keuzelijst voor de types van aansluitingskabel volgens de gebruikte verbinding."""
    naam = 'KlAansluitingskabel'
    label = 'Aansluitingskabel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitingskabel'
    definition = 'Keuzelijst voor de types van aansluitingskabel volgens de gebruikte verbinding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitingskabel'
    options = {
        'alarmkabel-2-10': KeuzelijstWaarde(invulwaarde='alarmkabel-2-10',
                                            label='Alarmkabel 2+10',
                                            status='ingebruik',
                                            definitie='Alarmkabel 2+10',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-10'),
        'alarmkabel-2-4': KeuzelijstWaarde(invulwaarde='alarmkabel-2-4',
                                           label='Alarmkabel 2+4',
                                           status='ingebruik',
                                           definitie='Alarmkabel 2+4',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-4'),
        'alarmkabel-2-6': KeuzelijstWaarde(invulwaarde='alarmkabel-2-6',
                                           label='Alarmkabel 2+6',
                                           status='ingebruik',
                                           definitie='Alarmkabel 2+6',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-6'),
        'alarmkabel-2-8': KeuzelijstWaarde(invulwaarde='alarmkabel-2-8',
                                           label='Alarmkabel 2+8',
                                           status='ingebruik',
                                           definitie='Alarmkabel 2+8',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-8'),
        'draadloos': KeuzelijstWaarde(invulwaarde='draadloos',
                                      label='Draadloos',
                                      status='ingebruik',
                                      definitie='Draadloos',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/draadloos'),
        'lihch': KeuzelijstWaarde(invulwaarde='lihch',
                                  label='LIHCH',
                                  status='ingebruik',
                                  definitie='LIHCH',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/lihch'),
        'lihh': KeuzelijstWaarde(invulwaarde='lihh',
                                 label='LIHH',
                                 status='ingebruik',
                                 definitie='LIHH',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/lihh'),
        'liycy': KeuzelijstWaarde(invulwaarde='liycy',
                                  label='LIYCY',
                                  status='ingebruik',
                                  definitie='LIYCY',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/liycy'),
        'liyy': KeuzelijstWaarde(invulwaarde='liyy',
                                 label='LIYY',
                                 status='ingebruik',
                                 definitie='LIYY',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/liyy'),
        'telefoonkabel': KeuzelijstWaarde(invulwaarde='telefoonkabel',
                                          label='Telefoonkabel',
                                          status='ingebruik',
                                          definitie='Telefoonkabel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/telefoonkabel'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                status='ingebruik',
                                definitie='UTP',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/utp'),
        'xgb': KeuzelijstWaarde(invulwaarde='xgb',
                                label='XGB',
                                status='ingebruik',
                                definitie='XGB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/xgb'),
        'xvb': KeuzelijstWaarde(invulwaarde='xvb',
                                label='XVB',
                                status='ingebruik',
                                definitie='XVB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingskabel/xvb')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

