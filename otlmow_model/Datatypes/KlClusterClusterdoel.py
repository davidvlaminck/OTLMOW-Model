# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlClusterClusterdoel(KeuzelijstField):
    """De reden waarom de custer is opgezet."""
    naam = 'KlClusterClusterdoel'
    label = 'Cluster clusterdoel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlClusterClusterdoel'
    definition = 'De reden waarom de custer is opgezet.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlClusterClusterdoel'
    options = {
        'groeperen-resources': KeuzelijstWaarde(invulwaarde='groeperen-resources',
                                                label='groeperen resources',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/groeperen-resources'),
        'redundantie': KeuzelijstWaarde(invulwaarde='redundantie',
                                        label='redundantie',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlClusterClusterdoel/redundantie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

