# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalSplitterModelnaam(KeuzelijstField):
    """De modelnaam van de signaalsplitter."""
    naam = 'KlSignaalSplitterModelnaam'
    label = 'Signaalsplitter modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalSplitterModelnaam'
    definition = 'De modelnaam van de signaalsplitter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalSplitterModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

