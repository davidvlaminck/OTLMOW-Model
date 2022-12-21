# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIPModuleTGCMerk(KeuzelijstField):
    """Lijst van merknamen van IP-modules voor toegangscontrole volgens de fabrikant."""
    naam = 'KlIPModuleTGCMerk'
    label = 'Merknamen IP-modules voor toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIPModuleTGCMerk'
    definition = 'Lijst van merknamen van IP-modules voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIPModuleTGCMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

