# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDoorrijhoogte(KeuzelijstField):
    """De mogelijke opties voor doorrijhoogte in meters."""
    naam = 'KlDoorrijhoogte'
    label = 'Doorrijhoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDoorrijhoogte'
    definition = 'De mogelijke opties voor doorrijhoogte in meters.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDoorrijhoogte'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

