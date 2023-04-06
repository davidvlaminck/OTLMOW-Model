# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVEenheidType(KeuzelijstField):
    """Mogelijke opties van eenheid types/"""
    naam = 'KlMIVEenheidType'
    label = 'MIV eenheid type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVEenheidType'
    definition = 'Mogelijke opties van eenheid types/'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVEenheidType'
    options = {
        'lve-19-inch': KeuzelijstWaarde(invulwaarde='lve-19-inch',
                                        label='LVE 19 inch',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch'),
        'lve-compact': KeuzelijstWaarde(invulwaarde='lve-compact',
                                        label='LVE compact',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-compact'),
        'lve-ip-detectoren': KeuzelijstWaarde(invulwaarde='lve-ip-detectoren',
                                              label='LVE IP-detectoren',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-ip-detectoren'),
        'lve-mini': KeuzelijstWaarde(invulwaarde='lve-mini',
                                     label='LVE MINI',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-mini'),
        'sat': KeuzelijstWaarde(invulwaarde='sat',
                                label='SAT',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/sat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

