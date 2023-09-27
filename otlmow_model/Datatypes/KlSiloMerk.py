# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSiloMerk(KeuzelijstField):
    """Het merk van de silo."""
    naam = 'KlSiloMerk'
    label = 'Silo merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSiloMerk'
    definition = 'Het merk van de silo.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSiloMerk'
    options = {
        'm-i-p': KeuzelijstWaarde(invulwaarde='m-i-p',
                                  label='M.I.P',
                                  status='ingebruik',
                                  definitie='M.I.P',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSiloMerk/m-i-p')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

