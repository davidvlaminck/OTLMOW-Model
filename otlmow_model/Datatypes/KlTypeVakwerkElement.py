# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVakwerkElement(KeuzelijstField):
    """Het type van vakwerk-element."""
    naam = 'KlTypeVakwerkElement'
    label = 'Type vakwerk-element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeVakwerkElement'
    definition = 'Het type van vakwerk-element.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVakwerkElement'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

