# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorMerk(KeuzelijstField):
    """Het merk van de weegsensor."""
    naam = 'KlWeegsensorMerk'
    label = 'Weegsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorMerk'
    definition = 'Het merk van de weegsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorMerk'
    options = {
        'Kistler': KeuzelijstWaarde(invulwaarde='Kistler',
                                    label='Kistler',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorMerk/Kistler')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

