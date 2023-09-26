# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
        'dmf-031': KeuzelijstWaarde(invulwaarde='dmf-031',
                                    label='DMF 031',
                                    status='ingebruik',
                                    definitie='DMF 031',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf-031'),
        'dmf-132': KeuzelijstWaarde(invulwaarde='dmf-132',
                                    label='DMF 132',
                                    status='ingebruik',
                                    definitie='DMF 132',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf-132'),
        'dmf-133': KeuzelijstWaarde(invulwaarde='dmf-133',
                                    label='DMF 133',
                                    status='ingebruik',
                                    definitie='DMF 133',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf-133'),
        'dmu703': KeuzelijstWaarde(invulwaarde='dmu703',
                                   label='DMU703',
                                   status='ingebruik',
                                   definitie='DMU703',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmu703')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

