# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSMerk(KeuzelijstField):
    """Het merk van de UPS."""
    naam = 'KlUPSMerk'
    label = 'UPS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSMerk'
    definition = 'Het merk van de UPS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSMerk'
    options = {
        'adelsystems': KeuzelijstWaarde(invulwaarde='adelsystems',
                                        label='AdelSystems',
                                        status='ingebruik',
                                        definitie='AdelSystems',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/adelsystems'),
        'eaton': KeuzelijstWaarde(invulwaarde='eaton',
                                  label='Eaton',
                                  status='ingebruik',
                                  definitie='Eaton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/eaton'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/phoenix-contact'),
        'prostar': KeuzelijstWaarde(invulwaarde='prostar',
                                    label='Prostar',
                                    status='ingebruik',
                                    definitie='Prostar',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/prostar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

