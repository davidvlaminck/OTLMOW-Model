# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijMerk(KeuzelijstField):
    """Het merk van de batterij."""
    naam = 'KlBatterijMerk'
    label = 'Batterij merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijMerk'
    definition = 'Het merk van de batterij.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijMerk'
    options = {
        'eco-counter': KeuzelijstWaarde(invulwaarde='eco-counter',
                                        label='eco-counter',
                                        status='ingebruik',
                                        definitie='eco-counter',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMerk/eco-counter'),
        'landport': KeuzelijstWaarde(invulwaarde='landport',
                                     label='landport',
                                     status='ingebruik',
                                     definitie='landport',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMerk/landport')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

