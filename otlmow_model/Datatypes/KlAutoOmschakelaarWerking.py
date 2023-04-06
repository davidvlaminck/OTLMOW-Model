# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAutoOmschakelaarWerking(KeuzelijstField):
    """Lijst met werkingsprincipes van automtische omschakelaars (transfer switches)."""
    naam = 'KlAutoOmschakelaarWerking'
    label = 'Automatische omschakelaar werkingsprincipe'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAutoOmschakelaarWerking'
    definition = 'Lijst met werkingsprincipes van automtische omschakelaars (transfer switches).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAutoOmschakelaarWerking'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

