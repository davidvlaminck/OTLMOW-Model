# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieelementStandplaats(KeuzelijstField):
    """De mogelijke standplaatsen van een vegetatieelement."""
    naam = 'KlVegetatieelementStandplaats'
    label = 'Vegetatieelement standplaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVegetatieelementStandplaats'
    definition = 'De mogelijke standplaatsen van een vegetatieelement.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieelementStandplaats'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

