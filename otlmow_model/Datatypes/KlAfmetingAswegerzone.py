# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


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
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

