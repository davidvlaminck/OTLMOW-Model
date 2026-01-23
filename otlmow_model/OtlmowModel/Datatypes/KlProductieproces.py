# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlProductieproces(KeuzelijstField):
    """De verschillende types van het productieproces van het kunststof object."""
    naam = 'KlProductieproces'
    label = 'KlProductieproces'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlProductieproces'
    definition = 'De verschillende types van het productieproces van het kunststof object.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlProductieproces'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

