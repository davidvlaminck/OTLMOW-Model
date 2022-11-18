# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugRijrichting(KeuzelijstField):
    """Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele)."""
    naam = 'KlSeinbrugRijrichting'
    label = 'Seinbrug rijrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugRijrichting'
    definition = 'Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugRijrichting'
    options = {
        'dubbele-rijrichting': KeuzelijstWaarde(invulwaarde='dubbele-rijrichting',
                                                label='dubbele rijrichting',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/dubbele-rijrichting'),
        'enkele-rijrichting': KeuzelijstWaarde(invulwaarde='enkele-rijrichting',
                                               label='enkele rijrichting',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/enkele-rijrichting')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

