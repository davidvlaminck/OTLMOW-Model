# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadiolistenerMerk(KeuzelijstField):
    """Merknaam van de radiolistener module."""
    naam = 'KlRadiolistenerMerk'
    label = 'Radiolistener merknaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadiolistenerMerk'
    definition = 'Merknaam van de radiolistener module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadiolistenerMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

