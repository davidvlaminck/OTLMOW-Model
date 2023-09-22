# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDompelpompModelnaam(KeuzelijstField):
    """Lijst van modelnamen van dompelpompen volgens de fabrikant."""
    naam = 'KlDompelpompModelnaam'
    label = 'Modelnamen dompelpompen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDompelpompModelnaam'
    definition = 'Lijst van modelnamen van dompelpompen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDompelpompModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

