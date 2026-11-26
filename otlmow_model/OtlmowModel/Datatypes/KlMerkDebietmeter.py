# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMerkDebietmeter(KeuzelijstField):
    """De verschillende merken van de debietmeter."""
    naam = 'KlMerkDebietmeter'
    label = 'Merk debietmeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMerkDebietmeter'
    definition = 'De verschillende merken van de debietmeter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMerkDebietmeter'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

