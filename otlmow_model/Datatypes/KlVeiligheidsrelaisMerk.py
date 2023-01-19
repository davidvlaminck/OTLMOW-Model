# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVeiligheidsrelaisMerk(KeuzelijstField):
    """Een lijst met merknamen van veiligheidsrelais volgens de fabrikant."""
    naam = 'KlVeiligheidsrelaisMerk'
    label = 'Veiligheidsrelais merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVeiligheidsrelaisMerk'
    definition = 'Een lijst met merknamen van veiligheidsrelais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVeiligheidsrelaisMerk'
    options = {
        'isotron': KeuzelijstWaarde(invulwaarde='isotron',
                                    label='ISOTRON',
                                    status='ingebruik',
                                    definitie='ISOTRON',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVeiligheidsrelaisMerk/isotron'),
        'phoenics': KeuzelijstWaarde(invulwaarde='phoenics',
                                     label='Phoenics',
                                     status='ingebruik',
                                     definitie='Phoenics',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVeiligheidsrelaisMerk/phoenics'),
        'pilz': KeuzelijstWaarde(invulwaarde='pilz',
                                 label='PILZ',
                                 status='ingebruik',
                                 definitie='PILZ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVeiligheidsrelaisMerk/pilz')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

