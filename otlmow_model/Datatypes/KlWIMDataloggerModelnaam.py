# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWIMDataloggerModelnaam(KeuzelijstField):
    """De modelnaam van de WIM-datalogger."""
    naam = 'KlWIMDataloggerModelnaam'
    label = 'WIM-datalogger modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWIMDataloggerModelnaam'
    definition = 'De modelnaam van de WIM-datalogger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWIMDataloggerModelnaam'
    options = {
        'wim-data-logger-5204ac04': KeuzelijstWaarde(invulwaarde='wim-data-logger-5204ac04',
                                                     label='WIM Data Logger 5204AC04',
                                                     status='ingebruik',
                                                     definitie='WIM Data Logger 5204AC04',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWIMDataloggerModelnaam/wim-data-logger-5204ac04')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

