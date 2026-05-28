# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPrimaireVormCombiwand(KeuzelijstField):
    """De mogelijke primaire vormen van een combiwand."""
    naam = 'KlPrimaireVormCombiwand'
    label = 'Primaire vorm combiwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPrimaireVormCombiwand'
    definition = 'De mogelijke primaire vormen van een combiwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPrimaireVormCombiwand'
    options = {
        'buis': KeuzelijstWaarde(invulwaarde='buis',
                                 label='Buis',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPrimaireVormCombiwand/buis'),
        'h-profiel': KeuzelijstWaarde(invulwaarde='h-profiel',
                                      label='H-profiel',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPrimaireVormCombiwand/h-profiel'),
        'stalen-caisson': KeuzelijstWaarde(invulwaarde='stalen-caisson',
                                           label='Stalen caisson',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPrimaireVormCombiwand/stalen-caisson')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

