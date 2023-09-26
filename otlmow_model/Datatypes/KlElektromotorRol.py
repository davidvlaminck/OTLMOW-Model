# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElektromotorRol(KeuzelijstField):
    """Keuzelijst voor de rol van de elektromotor in de aandrijflijn."""
    naam = 'KlElektromotorRol'
    label = 'Elektromotor rol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElektromotorRol'
    definition = 'Keuzelijst voor de rol van de elektromotor in de aandrijflijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElektromotorRol'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='Andere',
                                   status='ingebruik',
                                   definitie='Andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorRol/andere'),
        'hoofdmotor': KeuzelijstWaarde(invulwaarde='hoofdmotor',
                                       label='Hoofdmotor',
                                       status='ingebruik',
                                       definitie='Hoofdmotor',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorRol/hoofdmotor'),
        'hulpmotor': KeuzelijstWaarde(invulwaarde='hulpmotor',
                                      label='Hulpmotor',
                                      status='ingebruik',
                                      definitie='Hulpmotor',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorRol/hulpmotor'),
        'noodmotor': KeuzelijstWaarde(invulwaarde='noodmotor',
                                      label='Noodmotor',
                                      status='ingebruik',
                                      definitie='Noodmotor',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorRol/noodmotor')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

