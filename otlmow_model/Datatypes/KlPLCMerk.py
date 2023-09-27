# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCMerk(KeuzelijstField):
    """Het merk van de PLC."""
    naam = 'KlPLCMerk'
    label = 'PLC merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCMerk'
    definition = 'Het merk van de PLC.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCMerk'
    options = {
        'dtn': KeuzelijstWaarde(invulwaarde='dtn',
                                label='DTN',
                                status='ingebruik',
                                definitie='DTN',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/dtn'),
        'phoenics': KeuzelijstWaarde(invulwaarde='phoenics',
                                     label='Phoenics',
                                     status='ingebruik',
                                     definitie='Phoenics',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/phoenics'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/phoenix-contact'),
        'seneca': KeuzelijstWaarde(invulwaarde='seneca',
                                   label='SENECA',
                                   status='ingebruik',
                                   definitie='SENECA',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/seneca'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/siemens'),
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

