# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaar."""
    naam = 'KlPTRegelaarModelnaam'
    label = 'PT regelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPTRegelaarModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModelnaam'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

