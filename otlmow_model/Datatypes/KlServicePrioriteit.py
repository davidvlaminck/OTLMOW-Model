# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlServicePrioriteit(KeuzelijstField):
    """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden"""
    naam = 'KlServicePrioriteit'
    label = 'Serviceprioriteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlServicePrioriteit'
    definition = 'Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlServicePrioriteit'
    options = {
        'niet-prioritair': KeuzelijstWaarde(invulwaarde='niet-prioritair',
                                            label='niet prioritair',
                                            status='ingebruik',
                                            definitie='niet prioritair',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlServicePrioriteit/niet-prioritair'),
        'prioritair': KeuzelijstWaarde(invulwaarde='prioritair',
                                       label='prioritair',
                                       status='ingebruik',
                                       definitie='prioritair',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlServicePrioriteit/prioritair')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

