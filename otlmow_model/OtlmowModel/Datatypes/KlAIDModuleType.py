# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAIDModuleType(KeuzelijstField):
    """Het type van de AID-module."""
    naam = 'KlAIDModuleType'
    label = 'AID-module type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAIDModuleType'
    definition = 'Het type van de AID-module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIDModuleType'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

