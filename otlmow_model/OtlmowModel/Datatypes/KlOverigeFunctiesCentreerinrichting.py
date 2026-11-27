# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverigeFunctiesCentreerinrichting(KeuzelijstField):
    """De overige functies van de centreerinrichting."""
    naam = 'KlOverigeFunctiesCentreerinrichting'
    label = 'overige functies centreerinrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverigeFunctiesCentreerinrichting'
    definition = 'De overige functies van de centreerinrichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverigeFunctiesCentreerinrichting'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

