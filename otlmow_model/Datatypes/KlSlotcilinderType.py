# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotcilinderType(KeuzelijstField):
    """Keuzelijst voor het type slotcilinder."""
    naam = 'KlSlotcilinderType'
    label = 'Slotcilinder type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotcilinderType'
    definition = 'Keuzelijst voor het type slotcilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotcilinderType'
    options = {
        'edwa': KeuzelijstWaarde(invulwaarde='edwa',
                                 label='EDWA',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotcilinderType/edwa'),
        'isio': KeuzelijstWaarde(invulwaarde='isio',
                                 label='ISIO',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotcilinderType/isio')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

