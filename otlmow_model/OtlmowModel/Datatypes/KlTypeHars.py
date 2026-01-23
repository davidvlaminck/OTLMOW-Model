# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeHars(KeuzelijstField):
    """De verschillende types hars gebruikt in het kunststof object."""
    naam = 'KlTypeHars'
    label = 'type hars'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTypeHars'
    definition = 'De verschillende types hars gebruikt in het kunststof object.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeHars'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

