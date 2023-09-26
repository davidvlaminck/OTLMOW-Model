# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomMerk(KeuzelijstField):
    """Het merk van het intercomtoestel."""
    naam = 'KlIntercomMerk'
    label = 'Intercomtoestel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomMerk'
    definition = 'Het merk van het intercomtoestel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomMerk'
    options = {
        'nestor-company': KeuzelijstWaarde(invulwaarde='nestor-company',
                                           label='Nestor Company',
                                           status='ingebruik',
                                           definitie='Nestor Company',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIntercomMerk/nestor-company')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

