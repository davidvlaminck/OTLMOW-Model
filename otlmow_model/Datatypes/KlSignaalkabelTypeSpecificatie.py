# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelTypeSpecificatie(KeuzelijstField):
    """Lijst met mogelijke specificaties van het type van de signaalkabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlSignaalkabelTypeSpecificatie'
    label = 'Signaalkabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelTypeSpecificatie'
    definition = 'Lijst met mogelijke specificaties van het type van de signaalkabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelTypeSpecificatie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

