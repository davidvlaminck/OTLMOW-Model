# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtKARModemProtocol(KeuzelijstField):
    """Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren."""
    naam = 'KlPtKARModemProtocol'
    label = 'PT-KAR-modem protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtKARModemProtocol'
    definition = 'Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtKARModemProtocol'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

