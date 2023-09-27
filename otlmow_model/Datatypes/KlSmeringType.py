# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSmeringType(KeuzelijstField):
    """Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem."""
    naam = 'KlSmeringType'
    label = 'Smering type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSmeringType'
    definition = 'Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSmeringType'
    options = {
        'droog-lopend': KeuzelijstWaarde(invulwaarde='droog-lopend',
                                         label='droog lopend',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/droog-lopend'),
        'handmatig-te-smeren': KeuzelijstWaarde(invulwaarde='handmatig-te-smeren',
                                                label='handmatig te smeren',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/handmatig-te-smeren'),
        'met-automatische-smering': KeuzelijstWaarde(invulwaarde='met-automatische-smering',
                                                     label='met automatische smering',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/met-automatische-smering'),
        'zelf-smerend': KeuzelijstWaarde(invulwaarde='zelf-smerend',
                                         label='zelf smerend',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/zelf-smerend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

