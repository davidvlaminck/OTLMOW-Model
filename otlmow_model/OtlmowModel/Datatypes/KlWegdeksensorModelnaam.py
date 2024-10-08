# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegdeksensorModelnaam(KeuzelijstField):
    """Wegdeksensor modelnamen."""
    naam = 'KlWegdeksensorModelnaam'
    label = 'Wegdeksensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegdeksensorModelnaam'
    definition = 'Wegdeksensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegdeksensorModelnaam'
    options = {
        'drs511': KeuzelijstWaarde(invulwaarde='drs511',
                                   label='DRS511',
                                   status='ingebruik',
                                   definitie='DRS511',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdeksensorModelnaam/drs511')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

