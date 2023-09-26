# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOKaartModelnaam(KeuzelijstField):
    """Lijst van mogelijke modelnamen voor IO-kaarten."""
    naam = 'KlIOKaartModelnaam'
    label = 'IO-kaart modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOKaartModelnaam'
    definition = 'Lijst van mogelijke modelnamen voor IO-kaarten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOKaartModelnaam'
    options = {
        'dri50': KeuzelijstWaarde(invulwaarde='dri50',
                                  label='DRI50',
                                  status='ingebruik',
                                  definitie='DRI50',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/dri50'),
        'dri521': KeuzelijstWaarde(invulwaarde='dri521',
                                   label='DRI521',
                                   status='ingebruik',
                                   definitie='DRI521',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/dri521'),
        'dri701': KeuzelijstWaarde(invulwaarde='dri701',
                                   label='DRI701',
                                   status='ingebruik',
                                   definitie='DRI701',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/dri701'),
        'pma701': KeuzelijstWaarde(invulwaarde='pma701',
                                   label='PMA701',
                                   status='ingebruik',
                                   definitie='PMA701',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/pma701'),
        'pms701': KeuzelijstWaarde(invulwaarde='pms701',
                                   label='PMS701',
                                   status='ingebruik',
                                   definitie='PMS701',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/pms701'),
        'siu701': KeuzelijstWaarde(invulwaarde='siu701',
                                   label='SIU701',
                                   status='ingebruik',
                                   definitie='SIU701',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOKaartModelnaam/siu701')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

