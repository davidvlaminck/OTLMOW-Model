# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBelastingsklasse(KeuzelijstField):
    """De mogelijke belastingsklassen."""
    naam = 'KlBelastingsklasse'
    label = 'Belastingsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBelastingsklasse'
    definition = 'De mogelijke belastingsklassen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBelastingsklasse'
    options = {
        'a15': KeuzelijstWaarde(invulwaarde='a15',
                                label='a15',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/a15'),
        'b125': KeuzelijstWaarde(invulwaarde='b125',
                                 label='b125',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/b125'),
        'c250': KeuzelijstWaarde(invulwaarde='c250',
                                 label='c250',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/c250'),
        'd400': KeuzelijstWaarde(invulwaarde='d400',
                                 label='d400',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/d400'),
        'e600': KeuzelijstWaarde(invulwaarde='e600',
                                 label='e600',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/e600'),
        'f900': KeuzelijstWaarde(invulwaarde='f900',
                                 label='f900',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBelastingsklasse/f900')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

