# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelAdersEnSectie(KeuzelijstField):
    """Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een datakabel volgens het aantal aders en in voorkomende gevallen, hun dikte in vierkante millimeter."""
    naam = 'KlDatakabelAdersEnSectie'
    label = 'Datakabel aders en sectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelAdersEnSectie'
    definition = 'Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een datakabel volgens het aantal aders en in voorkomende gevallen, hun dikte in vierkante millimeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelAdersEnSectie'
    options = {
        '100-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='100-x-2-x-1-mm2',
                                            label='100 x 2 X 1 mm²',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/100-x-2-x-1-mm2'),
        '10x2x0.8': KeuzelijstWaarde(invulwaarde='10x2x0.8',
                                     label='10x2x0.8',
                                     status='ingebruik',
                                     definitie='10x2x0.8',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/10x2x0.8'),
        '20-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='20-x-2-x-1-mm2',
                                           label='20 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/20-x-2-x-1-mm2'),
        '21-x-2-x-1-mm2': KeuzelijstWaarde(invulwaarde='21-x-2-x-1-mm2',
                                           label='21 x 2 X 1 mm²',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/21-x-2-x-1-mm2'),
        '2x1.5': KeuzelijstWaarde(invulwaarde='2x1.5',
                                  label='2x1.5',
                                  status='ingebruik',
                                  definitie='2x1.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/2x1.5'),
        '2x2.5': KeuzelijstWaarde(invulwaarde='2x2.5',
                                  label='2x2.5',
                                  status='ingebruik',
                                  definitie='2x2.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/2x2.5'),
        '48-vezels': KeuzelijstWaarde(invulwaarde='48-vezels',
                                      label='48 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/48-vezels'),
        '4x2x1.5': KeuzelijstWaarde(invulwaarde='4x2x1.5',
                                    label='4x2x1.5',
                                    status='ingebruik',
                                    definitie='4x2x1.5',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/4x2x1.5'),
        '96-vezels': KeuzelijstWaarde(invulwaarde='96-vezels',
                                      label='96 vezels',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/96-vezels'),
        'zonder-verdere-specificatie': KeuzelijstWaarde(invulwaarde='zonder-verdere-specificatie',
                                                        label='zonder verdere specificatie',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelAdersEnSectie/zonder-verdere-specificatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

