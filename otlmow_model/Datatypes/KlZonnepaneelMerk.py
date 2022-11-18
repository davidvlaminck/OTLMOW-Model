# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonnepaneelMerk(KeuzelijstField):
    """Het merk van het zonnepaneel."""
    naam = 'KlZonnepaneelMerk'
    label = 'Zonnepaneel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZonnepaneelMerk'
    definition = 'Het merk van het zonnepaneel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonnepaneelMerk'
    options = {
        'solartronics': KeuzelijstWaarde(invulwaarde='solartronics',
                                         label='solartronics',
                                         status='ingebruik',
                                         definitie='solartronics ',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZonnepaneelMerk/solartronics')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

