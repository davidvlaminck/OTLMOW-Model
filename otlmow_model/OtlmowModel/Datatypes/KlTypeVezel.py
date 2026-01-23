# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVezel(KeuzelijstField):
    """De types vezel waaruit het kunststof object kan bestaan."""
    naam = 'KlTypeVezel'
    label = 'type vezel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTypeVezel'
    definition = 'De types vezel waaruit het kunststof object kan bestaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVezel'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

