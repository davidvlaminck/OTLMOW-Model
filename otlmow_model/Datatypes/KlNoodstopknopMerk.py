# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodstopknopMerk(KeuzelijstField):
    """Het merk van een noodstopknop."""
    naam = 'KlNoodstopknopMerk'
    label = 'Noodstopknop merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodstopknopMerk'
    definition = 'Het merk van een noodstopknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodstopknopMerk'
    options = {
        'isotron': KeuzelijstWaarde(invulwaarde='isotron',
                                    label='ISOTRON',
                                    status='ingebruik',
                                    definitie='ISOTRON',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/isotron'),
        'phoenics': KeuzelijstWaarde(invulwaarde='phoenics',
                                     label='Phoenics',
                                     status='uitgebruik',
                                     definitie='Phoenix',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/phoenics'),
        'phoenix': KeuzelijstWaarde(invulwaarde='phoenix',
                                    label='Phoenix',
                                    status='ingebruik',
                                    definitie='Phoenix',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/phoenix'),
        'pilz': KeuzelijstWaarde(invulwaarde='pilz',
                                 label='PILZ',
                                 status='ingebruik',
                                 definitie='PILZ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/pilz')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

