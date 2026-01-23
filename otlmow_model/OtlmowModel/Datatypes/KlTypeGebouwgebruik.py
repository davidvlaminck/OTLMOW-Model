# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGebouwgebruik(KeuzelijstField):
    """De mogelijke types van gebruik of functies van een gebouw."""
    naam = 'KlTypeGebouwgebruik'
    label = 'type gebouwgebruik'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeGebouwgebruik'
    definition = 'De mogelijke types van gebruik of functies van een gebouw.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGebouwgebruik'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

