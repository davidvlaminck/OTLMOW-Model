# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLuskaartType(KeuzelijstField):
    """Mogelijke types voor de uitvoering van luskaarten van Meten In Vlaanderen"""
    naam = 'KlMIVLuskaartType'
    label = 'MIV luskaart type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLuskaartType'
    definition = 'Mogelijke types voor de uitvoering van luskaarten van Meten In Vlaanderen'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLuskaartType'
    options = {
        '19-inch': KeuzelijstWaarde(invulwaarde='19-inch',
                                    label='19 inch',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLuskaartType/19-inch'),
        'compact': KeuzelijstWaarde(invulwaarde='compact',
                                    label='compact',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLuskaartType/compact'),
        'ip-detectoren': KeuzelijstWaarde(invulwaarde='ip-detectoren',
                                          label='IP-detectoren',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLuskaartType/ip-detectoren')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

