# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOntvangerModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Ontvanger."""
    naam = 'KlOntvangerModelnaam'
    label = 'ontvanger modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOntvangerModelnaam'
    definition = 'Keuzelijst met modelnamen voor Ontvanger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntvangerModelnaam'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

