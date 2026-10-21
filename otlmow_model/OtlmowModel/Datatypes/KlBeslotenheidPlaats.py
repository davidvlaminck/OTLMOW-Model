# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeslotenheidPlaats(KeuzelijstField):
    """De mogelijke plaatsen volgens de Camerawet, op basis van de beslotenheid en de toegankelijkheid voor het publiek."""
    naam = 'KlBeslotenheidPlaats'
    label = 'Beslotenheid plaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeslotenheidPlaats'
    definition = 'De mogelijke plaatsen volgens de Camerawet, op basis van de beslotenheid en de toegankelijkheid voor het publiek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeslotenheidPlaats'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

