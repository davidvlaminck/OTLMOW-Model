# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegcelModelnaam(KeuzelijstField):
    """Lijst met modelnamen van weegcellen."""
    naam = 'KlWeegcelModelnaam'
    label = 'Weegcel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegcelModelnaam'
    definition = 'Lijst met modelnamen van weegcellen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegcelModelnaam'
    options = {
        'gwt': KeuzelijstWaarde(invulwaarde='gwt',
                                label='GWT',
                                status='ingebruik',
                                definitie='GWT',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegcelModelnaam/gwt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

