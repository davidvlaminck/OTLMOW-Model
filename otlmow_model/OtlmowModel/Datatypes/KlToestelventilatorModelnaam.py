# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestelventilatorModelnaam(KeuzelijstField):
    """Lijst met modelnamen van ventilatoren gebruikt voor de koeling van toestellen."""
    naam = 'KlToestelventilatorModelnaam'
    label = 'Toestelventlaitor modelnamen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToestelventilatorModelnaam'
    definition = 'Lijst met modelnamen van ventilatoren gebruikt voor de koeling van toestellen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestelventilatorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

