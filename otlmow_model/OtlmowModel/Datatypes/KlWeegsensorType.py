# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorType(KeuzelijstField):
    """Het type van de weegsensor."""
    naam = 'KlWeegsensorType'
    label = 'Weegsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorType'
    definition = 'Het type van de weegsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorType'
    options = {
        'piëzo-kwarts': KeuzelijstWaarde(invulwaarde='piëzo-kwarts',
                                         label='piëzo-kwarts',
                                         status='ingebruik',
                                         definitie='piëzo-kwarts',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorType/piëzo-kwarts')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

