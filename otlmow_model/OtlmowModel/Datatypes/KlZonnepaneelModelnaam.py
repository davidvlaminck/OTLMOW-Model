# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonnepaneelModelnaam(KeuzelijstField):
    """De modelnaam van het zonnepaneel."""
    naam = 'KlZonnepaneelModelnaam'
    label = 'Zonnepaneel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZonnepaneelModelnaam'
    definition = 'De modelnaam van het zonnepaneel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonnepaneelModelnaam'
    options = {
        'pv': KeuzelijstWaarde(invulwaarde='pv',
                               label='PV',
                               status='ingebruik',
                               definitie='PV',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZonnepaneelModelnaam/pv')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

