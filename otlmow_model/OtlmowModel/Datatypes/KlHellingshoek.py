# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHellingshoek(KeuzelijstField):
    """De hellingshoek in graden."""
    naam = 'KlHellingshoek'
    label = 'Hellingshoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHellingshoek'
    definition = 'De hellingshoek in graden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHellingshoek'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

