# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordOpMaatMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van dynamische borden op maat. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordOpMaatMerk'
    label = 'Keuzelijst merknamen voor dynamische borden op maat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordOpMaatMerk'
    definition = 'Keuzelijst met de gangbare merken van dynamische borden op maat. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordOpMaatMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

