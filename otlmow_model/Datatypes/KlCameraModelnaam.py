# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraModelnaam(KeuzelijstField):
    """De modelnaam van de camera."""
    naam = 'KlCameraModelnaam'
    label = 'Camera modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraModelnaam'
    definition = 'De modelnaam van de camera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraModelnaam'
    options = {
        'b95a': KeuzelijstWaarde(invulwaarde='b95a',
                                 label='B95A',
                                 status='ingebruik',
                                 definitie='B95A',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/b95a'),
        'dinion-ip-starlight-8000-m': KeuzelijstWaarde(invulwaarde='dinion-ip-starlight-8000-m',
                                                       label='Dinion IP Starlight 8000 M',
                                                       status='ingebruik',
                                                       definitie='Dinion IP Starlight 8000 M',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/dinion-ip-starlight-8000-m'),
        'mic-ip-7100i': KeuzelijstWaarde(invulwaarde='mic-ip-7100i',
                                         label='MIC IP 7100i',
                                         status='ingebruik',
                                         definitie='MIC IP 7100i',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/mic-ip-7100i'),
        'mx-m16b': KeuzelijstWaarde(invulwaarde='mx-m16b',
                                    label='MX-M16B',
                                    status='ingebruik',
                                    definitie='MX-M16B',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/mx-m16b'),
        'q3515-lve-22mm': KeuzelijstWaarde(invulwaarde='q3515-lve-22mm',
                                           label='Q3515-LVE-22mm',
                                           status='ingebruik',
                                           definitie='Q3515-LVE-22mm',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/q3515-lve-22mm'),
        'q3515-lve-9mm': KeuzelijstWaarde(invulwaarde='q3515-lve-9mm',
                                          label='Q3515-LVE-9mm',
                                          status='ingebruik',
                                          definitie='Q3515-LVE-9mm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/q3515-lve-9mm'),
        'q3517-lve-22mm': KeuzelijstWaarde(invulwaarde='q3517-lve-22mm',
                                           label='Q3517-LVE-22mm',
                                           status='ingebruik',
                                           definitie='Q3517-LVE-22mm',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/q3517-lve-22mm'),
        'trafibot2': KeuzelijstWaarde(invulwaarde='trafibot2',
                                      label='TrafiBot2',
                                      status='ingebruik',
                                      definitie='TrafiBot2',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/trafibot2'),
        'ulisse-hd': KeuzelijstWaarde(invulwaarde='ulisse-hd',
                                      label='Ulisse HD',
                                      status='ingebruik',
                                      definitie='Ulisse HD',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/ulisse-hd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

