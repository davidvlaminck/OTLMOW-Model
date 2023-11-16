# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingskabelSectie(KeuzelijstField):
    """Lijst met mogelijke waarden voor de sectie van een aardingskabel."""
    naam = 'KlAardingskabelSectie'
    label = 'Aardingskabel sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlAardingskabelSectie'
    definition = 'Lijst met mogelijke waarden voor de sectie van een aardingskabel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingskabelSectie'
    options = {
        '10-mm2': KeuzelijstWaarde(invulwaarde='10-mm2',
                                   label='10 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/10-mm2'),
        '16': KeuzelijstWaarde(invulwaarde='16',
                               label='16',
                               status='ingebruik',
                               definitie='16',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/16'),
        '16-mm2': KeuzelijstWaarde(invulwaarde='16-mm2',
                                   label='16 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/16-mm2'),
        '1x10': KeuzelijstWaarde(invulwaarde='1x10',
                                 label='1x10',
                                 status='ingebruik',
                                 definitie='1x10',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/1x10'),
        '1x16': KeuzelijstWaarde(invulwaarde='1x16',
                                 label='1x16',
                                 status='ingebruik',
                                 definitie='1x16',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/1x16'),
        '1x25': KeuzelijstWaarde(invulwaarde='1x25',
                                 label='1x25',
                                 status='ingebruik',
                                 definitie='1x25',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/1x25'),
        '2.5-mm2': KeuzelijstWaarde(invulwaarde='2.5-mm2',
                                    label='2.5 mm²',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/2.5-mm2'),
        '25': KeuzelijstWaarde(invulwaarde='25',
                               label='25',
                               status='ingebruik',
                               definitie='25',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/25'),
        '25-mm2': KeuzelijstWaarde(invulwaarde='25-mm2',
                                   label='25 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/25-mm2'),
        '35-mm2': KeuzelijstWaarde(invulwaarde='35-mm2',
                                   label='35 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/35-mm2'),
        '4-mm2': KeuzelijstWaarde(invulwaarde='4-mm2',
                                  label='4 mm²',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/4-mm2'),
        '50-mm2': KeuzelijstWaarde(invulwaarde='50-mm2',
                                   label='50 mm²',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/50-mm2'),
        '6-mm2': KeuzelijstWaarde(invulwaarde='6-mm2',
                                  label='6 mm²',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/6-mm2'),
        '7x2x0.8': KeuzelijstWaarde(invulwaarde='7x2x0.8',
                                    label='7x2x0.8',
                                    status='ingebruik',
                                    definitie='7x2x0.8',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingskabelSectie/7x2x0.8')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

