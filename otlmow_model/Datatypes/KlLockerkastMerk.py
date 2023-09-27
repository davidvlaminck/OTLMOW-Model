# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLockerkastMerk(KeuzelijstField):
    """Het merk van de lockerkast."""
    naam = 'KlLockerkastMerk'
    label = 'Lockerkast merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLockerkastMerk'
    definition = 'Het merk van de lockerkast.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLockerkastMerk'
    options = {
        'inox-rvs': KeuzelijstWaarde(invulwaarde='inox-rvs',
                                     label='INOX-RVS',
                                     status='ingebruik',
                                     definitie='INOX-RVS',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLockerkastMerk/inox-rvs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

