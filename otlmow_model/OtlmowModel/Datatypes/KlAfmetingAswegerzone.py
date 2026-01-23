# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        '15m': KeuzelijstWaarde(invulwaarde='15m',
                                label='15m',
                                status='ingebruik',
                                definitie='15 meter',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingAswegerzone/15m'),
        '20m': KeuzelijstWaarde(invulwaarde='20m',
                                label='20m',
                                status='ingebruik',
                                definitie='20 meter',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingAswegerzone/20m')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

