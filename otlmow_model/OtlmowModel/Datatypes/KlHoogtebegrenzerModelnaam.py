# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtebegrenzerModelnaam(KeuzelijstField):
    """De mogelijke modelnamen van een hoogtebegrenzer."""
    naam = 'KlHoogtebegrenzerModelnaam'
    label = 'Hoogtebegrenzer modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtebegrenzerModelnaam'
    definition = 'De mogelijke modelnamen van een hoogtebegrenzer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtebegrenzerModelnaam'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

