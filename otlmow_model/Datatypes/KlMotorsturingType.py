# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorsturingType(KeuzelijstField):
    """Lijst met types van motorsturingen"""
    naam = 'KlMotorsturingType'
    label = 'Types motorsturing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorsturingType'
    definition = 'Lijst met types van motorsturingen'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorsturingType'
    options = {
        'dc-motorsturing': KeuzelijstWaarde(invulwaarde='dc-motorsturing',
                                            label='DC motorsturing',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorsturingType/dc-motorsturing'),
        'frequentiesturing': KeuzelijstWaarde(invulwaarde='frequentiesturing',
                                              label='frequentiesturing',
                                              status='ingebruik',
                                              definitie='Elektronische vermogenschakelaar die een bepaalde uitgangsspanning met een bepaalde frequentie realiseert. Deze frequentie is onder andere bepalend voor snelheid/toerental van de elektromotor.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorsturingType/frequentiesturing'),
        'softstarter': KeuzelijstWaarde(invulwaarde='softstarter',
                                        label='softstarter',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorsturingType/softstarter')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

