# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPoEInjectorMerk(KeuzelijstField):
    """Het merk van de PoE-injector."""
    naam = 'KlPoEInjectorMerk'
    label = 'Power over ethernet injector merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPoEInjectorMerk'
    definition = 'Het merk van de PoE-injector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPoEInjectorMerk'
    options = {
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoEInjectorMerk/bosch'),
        'planet': KeuzelijstWaarde(invulwaarde='planet',
                                   label='PLANET',
                                   status='ingebruik',
                                   definitie='PLANET',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoEInjectorMerk/planet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

