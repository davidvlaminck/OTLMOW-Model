# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVeiligheidsrelaisModelnaam(KeuzelijstField):
    """Een lijst met modelnamen van veilgheidsrelais volgens de fabrikant."""
    naam = 'KlVeiligheidsrelaisModelnaam'
    label = 'Veiligheidsrelais modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVeiligheidsrelaisModelnaam'
    definition = 'Een lijst met modelnamen van veilgheidsrelais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVeiligheidsrelaisModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

