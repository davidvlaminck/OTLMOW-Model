# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrostatischeNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de hydrostatische niveaumeting."""
    naam = 'KlHydrostatischeNiveaumetingMerk'
    label = 'Hydrostatische niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrostatischeNiveaumetingMerk'
    definition = 'Merknamen van de hydrostatische niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrostatischeNiveaumetingMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

