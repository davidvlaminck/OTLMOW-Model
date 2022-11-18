# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverProtocol(KeuzelijstField):
    """Protocol gebruikt door de LED driver voor het aansturen van de LED's."""
    naam = 'KlLEDDriverProtocol'
    label = 'LED stuurprotocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverProtocol'
    definition = "Protocol gebruikt door de LED driver voor het aansturen van de LED's."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverProtocol'
    options = {
        '1-10v': KeuzelijstWaarde(invulwaarde='1-10v',
                                  label='1-10v',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/1-10v'),
        'dali': KeuzelijstWaarde(invulwaarde='dali',
                                 label='dali',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/dali'),
        'daliv2': KeuzelijstWaarde(invulwaarde='daliv2',
                                   label='daliv2',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverProtocol/daliv2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

