# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFlensType(KeuzelijstField):
    """Keuzelijst met de types flensen."""
    naam = 'KlFlensType'
    label = 'Flens type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFlensType'
    definition = 'Keuzelijst met de types flensen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFlensType'
    options = {
        'blindflens': KeuzelijstWaarde(invulwaarde='blindflens',
                                       label='blindflens',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFlensType/blindflens'),
        'overschuifflens': KeuzelijstWaarde(invulwaarde='overschuifflens',
                                            label='overschuifflens',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFlensType/overschuifflens'),
        'vlakkelasflens': KeuzelijstWaarde(invulwaarde='vlakkelasflens',
                                           label='vlakkelasflens',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFlensType/vlakkelasflens'),
        'voorlasflens': KeuzelijstWaarde(invulwaarde='voorlasflens',
                                         label='voorlasflens',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFlensType/voorlasflens')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

