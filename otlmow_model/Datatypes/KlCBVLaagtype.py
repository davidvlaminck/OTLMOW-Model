# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVLaagtype(KeuzelijstField):
    """Bepaling van het laagtype van de cement/beton verharding."""
    naam = 'KlCBVLaagtype'
    label = 'CBV laagtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVLaagtype'
    definition = 'Bepaling van het laagtype van de cement/beton verharding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVLaagtype'
    options = {
        'eenlaagse-betonverharding': KeuzelijstWaarde(invulwaarde='eenlaagse-betonverharding',
                                                      label='eenlaagse betonverharding',
                                                      status='ingebruik',
                                                      definitie='Betonverharding die in één laag aangelegd wordt. ',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVLaagtype/eenlaagse-betonverharding'),
        'tweelaagse-betonverharding': KeuzelijstWaarde(invulwaarde='tweelaagse-betonverharding',
                                                       label='tweelaagse betonverharding',
                                                       status='ingebruik',
                                                       definitie='Betonverharding die in twee lagen aangelegd wordt. ',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVLaagtype/tweelaagse-betonverharding')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

