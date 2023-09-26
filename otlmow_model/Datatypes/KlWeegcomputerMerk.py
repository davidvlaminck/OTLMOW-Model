# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegcomputerMerk(KeuzelijstField):
    """De merknaam van het toestel volgens de fabrikant."""
    naam = 'KlWeegcomputerMerk'
    label = 'Weegcomputer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegcomputerMerk'
    definition = 'De merknaam van het toestel volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegcomputerMerk'
    options = {
        'minebea-intec': KeuzelijstWaarde(invulwaarde='minebea-intec',
                                          label='Minebea intec',
                                          status='ingebruik',
                                          definitie='Minebea intec',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegcomputerMerk/minebea-intec')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

