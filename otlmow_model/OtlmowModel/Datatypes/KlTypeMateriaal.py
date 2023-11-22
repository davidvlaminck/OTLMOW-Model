# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeMateriaal(KeuzelijstField):
    """Keuzelijst om aan te geven welk materiaal gebruikt wordt voor de voeg tot stand te brengen."""
    naam = 'KlTypeMateriaal'
    label = 'Type materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeMateriaal'
    definition = 'Keuzelijst om aan te geven welk materiaal gebruikt wordt voor de voeg tot stand te brengen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeMateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)
