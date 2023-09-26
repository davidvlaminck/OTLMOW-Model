# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingAswegerzone(KeuzelijstField):
    """De afmeting in meter van de zone aangelegd voor en na de asweger die de voertuigen gebruiken."""
    naam = 'KlAfmetingAswegerzone'
    label = 'Afmeting asweger zone'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingAswegerzone'
    definition = 'De afmeting in meter van de zone aangelegd voor en na de asweger die de voertuigen gebruiken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingAswegerzone'
    options = {
        '35': KeuzelijstWaarde(invulwaarde='35',
                               label='35',
                               status='ingebruik',
                               definitie='Een zone met twee aanrijzones van 15 meter en een weegzone van ongeveer 5 meter.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingAswegerzone/35')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

