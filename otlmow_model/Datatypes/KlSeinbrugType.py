# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugType(KeuzelijstField):
    """Types van seinbrug."""
    naam = 'KlSeinbrugType'
    label = 'Seinbrug type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugType'
    definition = 'Types van seinbrug.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugType'
    options = {
        'enkeleLigger': KeuzelijstWaarde(invulwaarde='enkeleLigger',
                                         label='enkeleLigger',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/enkeleLigger'),
        'koker': KeuzelijstWaarde(invulwaarde='koker',
                                  label='koker',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/koker'),
        'nietDoorlopendeBuis': KeuzelijstWaarde(invulwaarde='nietDoorlopendeBuis',
                                                label='nietDoorlopendeBuis',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/nietDoorlopendeBuis'),
        'vakwerk': KeuzelijstWaarde(invulwaarde='vakwerk',
                                    label='vakwerk',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugType/vakwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

