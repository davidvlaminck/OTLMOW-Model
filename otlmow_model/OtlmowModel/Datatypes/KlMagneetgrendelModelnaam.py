# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMagneetgrendelModelnaam(KeuzelijstField):
    """Lijst van modelnamen van magneetgrendels volgens de fabrikant."""
    naam = 'KlMagneetgrendelModelnaam'
    label = 'Modelnamen magneetgrendels'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMagneetgrendelModelnaam'
    definition = 'Lijst van modelnamen van magneetgrendels volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMagneetgrendelModelnaam'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

