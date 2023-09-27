# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegcelMerk(KeuzelijstField):
    """Lijst met merknamen va weegcellen."""
    naam = 'KlWeegcelMerk'
    label = 'Weegcel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegcelMerk'
    definition = 'Lijst met merknamen va weegcellen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegcelMerk'
    options = {
        'logicontrol': KeuzelijstWaarde(invulwaarde='logicontrol',
                                        label='Logicontrol',
                                        status='ingebruik',
                                        definitie='Logicontrol',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegcelMerk/logicontrol'),
        'pr3221-125t-c3': KeuzelijstWaarde(invulwaarde='pr3221-125t-c3',
                                           label='PR3221/125t C3',
                                           status='ingebruik',
                                           definitie='PR3221/125t C3',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegcelMerk/pr3221-125t-c3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

