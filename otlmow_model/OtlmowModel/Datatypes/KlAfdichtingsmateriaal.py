# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfdichtingsmateriaal(KeuzelijstField):
    """Het afdichtingsmateriaal dat gebruikt wordt in de kabelleidingdoorvoer."""
    naam = 'KlAfdichtingsmateriaal'
    label = 'afdichtingsmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfdichtingsmateriaal'
    definition = 'Het afdichtingsmateriaal dat gebruikt wordt in de kabelleidingdoorvoer.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfdichtingsmateriaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

