# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDBordCommprotocol(KeuzelijstField):
    """De mogelijke opties voor het communicatieprotocol gebruikt bij de aansturing van een LEDBord type."""
    naam = 'KlLEDBordCommprotocol'
    label = 'LEDBord communicatieprotocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLEDBordCommprotocol'
    definition = 'De mogelijke opties voor het communicatieprotocol gebruikt bij de aansturing van een LEDBord type.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDBordCommprotocol'
    options = {
        'ethernet': KeuzelijstWaarde(invulwaarde='ethernet',
                                     label='ethernet',
                                     status='ingebruik',
                                     definitie='ethernet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDBordCommprotocol/ethernet'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='ingebruik',
                                    definitie='serieel',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDBordCommprotocol/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

