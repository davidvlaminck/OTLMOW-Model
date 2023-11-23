# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestelventilatorMerk(KeuzelijstField):
    """Lijst met merknamen van ventilatoren gebruikt voor de koeling van toestellen."""
    naam = 'KlToestelventilatorMerk'
    label = 'Toestelventilator merknamen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToestelventilatorMerk'
    definition = 'Lijst met merknamen van ventilatoren gebruikt voor de koeling van toestellen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestelventilatorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

