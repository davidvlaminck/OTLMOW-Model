# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVerankeringBrugdekvoeg(KeuzelijstField):
    """Het type van de verankering van de brugdekvoeg."""
    naam = 'KlTypeVerankeringBrugdekvoeg'
    label = 'Type verankering brugdekvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVerankeringBrugdekvoeg'
    definition = 'Het type van de verankering van de brugdekvoeg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVerankeringBrugdekvoeg'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

