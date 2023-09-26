# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitingDamwandBestaandeConstructie(KeuzelijstField):
    """De aansluiting van de damwand op een bestaande constructie."""
    naam = 'KlAansluitingDamwandBestaandeConstructie'
    label = 'Aansluiting damwand bestaande constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitingDamwandBestaandeConstructie'
    definition = 'De aansluiting van de damwand op een bestaande constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitingDamwandBestaandeConstructie'
    options = {
        'door-middel-van-betonprop': KeuzelijstWaarde(invulwaarde='door-middel-van-betonprop',
                                                      label='door middel van betonprop',
                                                      status='ingebruik',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingDamwandBestaandeConstructie/door-middel-van-betonprop'),
        'door-middel-van-groutprop': KeuzelijstWaarde(invulwaarde='door-middel-van-groutprop',
                                                      label='door middel van groutprop',
                                                      status='ingebruik',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingDamwandBestaandeConstructie/door-middel-van-groutprop'),
        'door-middel-van-kleiprop': KeuzelijstWaarde(invulwaarde='door-middel-van-kleiprop',
                                                     label='door middel van kleiprop',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingDamwandBestaandeConstructie/door-middel-van-kleiprop'),
        'door-middel-van-vrijzittend-slot': KeuzelijstWaarde(invulwaarde='door-middel-van-vrijzittend-slot',
                                                             label='door middel van vrijzittend slot',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitingDamwandBestaandeConstructie/door-middel-van-vrijzittend-slot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

