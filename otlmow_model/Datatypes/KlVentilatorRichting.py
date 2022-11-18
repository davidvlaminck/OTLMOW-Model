# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVentilatorRichting(KeuzelijstField):
    """Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden."""
    naam = 'KlVentilatorRichting'
    label = 'Ventilator richting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorRichting'
    definition = 'Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorRichting'
    options = {
        'bidirectioneel': KeuzelijstWaarde(invulwaarde='bidirectioneel',
                                           label='bidirectioneel',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/bidirectioneel'),
        'unidirectioneel': KeuzelijstWaarde(invulwaarde='unidirectioneel',
                                            label='unidirectioneel',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/unidirectioneel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

