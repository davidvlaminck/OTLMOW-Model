# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurmoduleTGCMerk(KeuzelijstField):
    """Lijst van merknamen van deurmodules voor toegangscontrole volgens de fabrikant."""
    naam = 'KlDeurmoduleTGCMerk'
    label = 'Merknamen deurmodules toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDeurmoduleTGCMerk'
    definition = 'Lijst van merknamen van deurmodules voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurmoduleTGCMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

