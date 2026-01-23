# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBevestigingLadder(KeuzelijstField):
    """De verschillende wijzen waarop een ladder aan een constructie bevestigd kan worden."""
    naam = 'KlTypeBevestigingLadder'
    label = 'type bevesting ladder'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBevestigingLadder'
    definition = 'De verschillende wijzen waarop een ladder aan een constructie bevestigd kan worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBevestigingLadder'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

