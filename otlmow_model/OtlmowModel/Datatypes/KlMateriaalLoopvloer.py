# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalLoopvloer(KeuzelijstField):
    """De keuzelijst die de verschillende type van materialen van de loopvloer bevat."""
    naam = 'KlMateriaalLoopvloer'
    label = 'Keuzelijst materiaal loopvloer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalLoopvloer'
    definition = 'De keuzelijst die de verschillende type van materialen van de loopvloer bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalLoopvloer'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/beton'),
        'cortenstaal': KeuzelijstWaarde(invulwaarde='cortenstaal',
                                        label='cortenstaal',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/cortenstaal'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/kunststof'),
        'roestvaststaal': KeuzelijstWaarde(invulwaarde='roestvaststaal',
                                           label='roestvaststaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/roestvaststaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalLoopvloer/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

