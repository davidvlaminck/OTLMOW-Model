# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerklocatie(KeuzelijstField):
    """De verschillende types netwerklocatie."""
    naam = 'KlNetwerklocatie'
    label = 'Keuzelijst Netwerklocatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerklocatie'
    definition = 'De verschillende types netwerklocatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerklocatie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

