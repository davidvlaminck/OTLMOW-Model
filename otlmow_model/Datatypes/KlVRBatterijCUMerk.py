# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVRBatterijCUMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor VRBatterijCU."""
    naam = 'KlVRBatterijCUMerk'
    label = 'Batterij CU merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVRBatterijCUMerk'
    definition = 'Keuzelijst met merknamen voor VRBatterijCU.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVRBatterijCUMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

