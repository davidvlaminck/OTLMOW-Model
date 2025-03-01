# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        'esprit-compact': KeuzelijstWaarde(invulwaarde='esprit-compact',
                                           label='Esprit Compact',
                                           status='ingebruik',
                                           definitie='Esprit Compact',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/esprit-compact'),
        'g3': KeuzelijstWaarde(invulwaarde='g3',
                               label='G3',
                               status='ingebruik',
                               definitie='G3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/g3'),
        'icar-cam5': KeuzelijstWaarde(invulwaarde='icar-cam5',
                                      label='iCar cam5',
                                      status='ingebruik',
                                      definitie='iCar cam5',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/icar-cam5'),
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
        'pelco-esprit-compact': KeuzelijstWaarde(invulwaarde='pelco-esprit-compact',
                                                 label='Pelco Esprit Compact',
                                                 status='uitgebruik',
                                                 definitie='Pelco Esprit Compact',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/pelco-esprit-compact'),
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
        'q3536-lve-9mm': KeuzelijstWaarde(invulwaarde='q3536-lve-9mm',
                                          label='Q3536-LVE-9mm',
                                          status='ingebruik',
                                          definitie='Q3536-LVE-9mm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/q3536-lve-9mm'),
        'trafibot': KeuzelijstWaarde(invulwaarde='trafibot',
                                     label='TrafiBot',
                                     status='ingebruik',
                                     definitie='TrafiBot',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/trafibot'),
        'trafibot-ai': KeuzelijstWaarde(invulwaarde='trafibot-ai',
                                        label='TrafiBot AI',
                                        status='ingebruik',
                                        definitie='TrafiBot AI',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/trafibot-ai'),
        'trafibot2': KeuzelijstWaarde(invulwaarde='trafibot2',
                                      label='TrafiBot2',
                                      status='ingebruik',
                                      definitie='TrafiBot2',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/trafibot2'),
        'ulisse-evo': KeuzelijstWaarde(invulwaarde='ulisse-evo',
                                       label='Ulisse EVO',
                                       status='ingebruik',
                                       definitie='Ulisse EVO',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/ulisse-evo'),
        'ulisse-hd': KeuzelijstWaarde(invulwaarde='ulisse-hd',
                                      label='Ulisse HD',
                                      status='ingebruik',
                                      definitie='Ulisse HD',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/ulisse-hd'),
        'vega-tasc': KeuzelijstWaarde(invulwaarde='vega-tasc',
                                      label='VEGA TaSC',
                                      status='ingebruik',
                                      definitie='VEGA TaSC',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraModelnaam/vega-tasc')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

