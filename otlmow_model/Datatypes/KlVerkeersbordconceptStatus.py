# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordconceptStatus(KeuzelijstField):
    """Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt."""
    naam = 'KlVerkeersbordconceptStatus'
    label = 'VerkeersbordconceptStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordconceptStatus'
    definition = 'Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordconceptStatus'
    options = {
        'afgeschaft': KeuzelijstWaarde(invulwaarde='afgeschaft',
                                       label='afgeschaft',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/afgeschaft'),
        'blabla': KeuzelijstWaarde(invulwaarde='blabla',
                                   label='blabla',
                                   status='ingebruik',
                                   definitie='qsfsd',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/blabla'),
        'stabiel': KeuzelijstWaarde(invulwaarde='stabiel',
                                    label='stabiel',
                                    status='ingebruik',
                                    definitie='tstst',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/stabiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

