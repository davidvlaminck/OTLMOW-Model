# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneFrequentierange(KeuzelijstField):
    """Keuzelijst met frequentiebanden aan waarbinnen een antenne gebruikt kan worden."""
    naam = 'KlAntenneFrequentierange'
    label = 'Antenne frequentierange'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneFrequentierange'
    definition = 'Keuzelijst met frequentiebanden aan waarbinnen een antenne gebruikt kan worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneFrequentierange'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

