# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordGrootteorde(KeuzelijstField):
    """Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250."""
    naam = 'KlRetroreflecterendVerkeersbordGrootteorde'
    label = 'Retroreflecterend verkeersbord grootteorde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordGrootteorde'
    definition = 'Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordGrootteorde'
    options = {
        'groot': KeuzelijstWaarde(invulwaarde='groot',
                                  label='groot',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/groot'),
        'klein': KeuzelijstWaarde(invulwaarde='klein',
                                  label='klein',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/klein'),
        'middelgroot': KeuzelijstWaarde(invulwaarde='middelgroot',
                                        label='middelgroot',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/middelgroot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

