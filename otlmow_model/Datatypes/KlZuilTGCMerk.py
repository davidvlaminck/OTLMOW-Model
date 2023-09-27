# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZuilTGCMerk(KeuzelijstField):
    """Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant."""
    naam = 'KlZuilTGCMerk'
    label = 'Merknamen zuilen toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZuilTGCMerk'
    definition = 'Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZuilTGCMerk'
    options = {
        'nestor-company': KeuzelijstWaarde(invulwaarde='nestor-company',
                                           label='Nestor Company',
                                           status='ingebruik',
                                           definitie='Nestor Company',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZuilTGCMerk/nestor-company')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

