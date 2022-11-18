# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareDomein(KeuzelijstField):
    """Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""
    naam = 'KlHardwareDomein'
    label = 'Hardware domein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareDomein'
    definition = 'Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareDomein'
    options = {
        'alfa': KeuzelijstWaarde(invulwaarde='alfa',
                                 label='alfa',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/alfa'),
        'belfla': KeuzelijstWaarde(invulwaarde='belfla',
                                   label='belfla',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareDomein/belfla')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

