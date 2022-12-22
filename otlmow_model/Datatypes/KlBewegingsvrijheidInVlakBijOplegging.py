# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBewegingsvrijheidInVlakBijOplegging(KeuzelijstField):
    """De bewegingsvrijheid in het vlak bij een oplegging."""
    naam = 'KlBewegingsvrijheidInVlakBijOplegging'
    label = 'Bewegingsvrijheid in vlak bij oplegging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBewegingsvrijheidInVlakBijOplegging'
    definition = 'De bewegingsvrijheid in het vlak bij een oplegging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBewegingsvrijheidInVlakBijOplegging'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

