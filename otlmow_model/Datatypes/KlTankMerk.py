# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankMerk(KeuzelijstField):
    """Het merk van de tank."""
    naam = 'KlTankMerk'
    label = 'Tank merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankMerk'
    definition = 'Het merk van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankMerk'
    options = {
        'm-i-p': KeuzelijstWaarde(invulwaarde='m-i-p',
                                  label='M.I.P',
                                  status='ingebruik',
                                  definitie='M.I.P',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMerk/m-i-p')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

