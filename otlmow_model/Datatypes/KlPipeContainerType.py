# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPipeContainerType(KeuzelijstField):
    """Lijst met types van pies voor het oude AKELA-type Pipe."""
    naam = 'KlPipeContainerType'
    label = 'Pipe container type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlPipeContainerType'
    definition = 'Lijst met types van pies voor het oude AKELA-type Pipe.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPipeContainerType'
    options = {
        'kabelenleidinggoot': KeuzelijstWaarde(invulwaarde='kabelenleidinggoot',
                                               label='kabelEnLeidingGoot',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPipeContainerType/kabelenleidinggoot'),
        'mantelbuis': KeuzelijstWaarde(invulwaarde='mantelbuis',
                                       label='mantelbuis',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPipeContainerType/mantelbuis')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

