# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlControlepaneelModelnaam(KeuzelijstField):
    """De modelnaam van het controlepaneel"""
    naam = 'KlControlepaneelModelnaam'
    label = 'Controlepaneel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlControlepaneelModelnaam'
    definition = 'De modelnaam van het controlepaneel'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlControlepaneelModelnaam'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

