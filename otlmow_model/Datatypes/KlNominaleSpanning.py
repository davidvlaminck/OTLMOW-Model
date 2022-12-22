# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNominaleSpanning(KeuzelijstField):
    """Keuzelijst voor de nominale spanning van een elektrische installatie."""
    naam = 'KlNominaleSpanning'
    label = 'Nominale spanning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNominaleSpanning'
    definition = 'Keuzelijst voor de nominale spanning van een elektrische installatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNominaleSpanning'
    options = {
        '12v': KeuzelijstWaarde(invulwaarde='12v',
                                label='12V',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/12v'),
        '230v': KeuzelijstWaarde(invulwaarde='230v',
                                 label='230V',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/230v'),
        '24v': KeuzelijstWaarde(invulwaarde='24v',
                                label='24V',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/24v'),
        '400v': KeuzelijstWaarde(invulwaarde='400v',
                                 label='400V',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/400v'),
        '660v': KeuzelijstWaarde(invulwaarde='660v',
                                 label='660V',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/660v'),
        '6kv': KeuzelijstWaarde(invulwaarde='6kv',
                                label='6kV',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNominaleSpanning/6kv')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

