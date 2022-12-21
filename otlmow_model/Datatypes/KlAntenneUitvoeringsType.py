# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneUitvoeringsType(KeuzelijstField):
    """Het uitvoeringstype van een antenne bepaalt de richting(en) waarover de antenne signaal kan ontvangen en uitsturen."""
    naam = 'KlAntenneUitvoeringsType'
    label = 'Antenne uitvoeringstype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneUitvoeringsType'
    definition = 'Het uitvoeringstype van een antenne bepaalt de richting(en) waarover de antenne signaal kan ontvangen en uitsturen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneUitvoeringsType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

