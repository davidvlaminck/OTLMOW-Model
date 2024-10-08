# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCModelnaam(KeuzelijstField):
    """De modelnaam van de PLC."""
    naam = 'KlPLCModelnaam'
    label = 'PLC model'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCModelnaam'
    definition = 'De modelnaam van de PLC.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCModelnaam'
    options = {
        'axc-f-3152': KeuzelijstWaarde(invulwaarde='axc-f-3152',
                                       label='AXC-F-3152',
                                       status='ingebruik',
                                       definitie='AXC-F-3152',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/axc-f-3152'),
        'dmu703': KeuzelijstWaarde(invulwaarde='dmu703',
                                   label='DMU703',
                                   status='ingebruik',
                                   definitie='DMU703',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmu703')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

