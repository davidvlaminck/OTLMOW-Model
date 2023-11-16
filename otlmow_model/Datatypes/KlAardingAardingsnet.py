# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingAardingsnet(KeuzelijstField):
    """Lijst van voorkomende types aardingsnet"""
    naam = 'KlAardingAardingsnet'
    label = 'Aardingsinstallatie aardingsnet'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAardingAardingsnet'
    definition = 'Lijst van voorkomende types aardingsnet'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingAardingsnet'
    options = {
        'it': KeuzelijstWaarde(invulwaarde='it',
                               label='IT',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/it'),
        'tnc': KeuzelijstWaarde(invulwaarde='tnc',
                                label='TNC',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/tnc'),
        'tncs': KeuzelijstWaarde(invulwaarde='tncs',
                                 label='TNCS',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/tncs'),
        'tns': KeuzelijstWaarde(invulwaarde='tns',
                                label='TNS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/tns'),
        'tns-tncs': KeuzelijstWaarde(invulwaarde='tns-tncs',
                                     label='TNS-TNCS',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/tns-tncs'),
        'tt': KeuzelijstWaarde(invulwaarde='tt',
                               label='TT',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingAardingsnet/tt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

