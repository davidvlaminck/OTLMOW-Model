# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestelventilatorFilterdoekKlasse(KeuzelijstField):
    """Keuzelijst die de verschillende filterklasses van een filterdoek voor een toestelventilator bevat."""
    naam = 'KlToestelventilatorFilterdoekKlasse'
    label = 'Toestelventilator filterdoek klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToestelventilatorFilterdoekKlasse'
    definition = 'Keuzelijst die de verschillende filterklasses van een filterdoek voor een toestelventilator bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestelventilatorFilterdoekKlasse'
    options = {
        'f7': KeuzelijstWaarde(invulwaarde='f7',
                               label='F7',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestelventilatorFilterdoekKlasse/f7'),
        'g3': KeuzelijstWaarde(invulwaarde='g3',
                               label='G3',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestelventilatorFilterdoekKlasse/g3'),
        'g4': KeuzelijstWaarde(invulwaarde='g4',
                               label='G4',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestelventilatorFilterdoekKlasse/g4'),
        'm5': KeuzelijstWaarde(invulwaarde='m5',
                               label='M5',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestelventilatorFilterdoekKlasse/m5'),
        'm6': KeuzelijstWaarde(invulwaarde='m6',
                               label='M6',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestelventilatorFilterdoekKlasse/m6')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

