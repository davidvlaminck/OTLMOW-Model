# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPDUMerk(KeuzelijstField):
    """Lijst van merknamen van stroomverdelingssystemen (Power Distribution Unit) volgens de fabrikant."""
    naam = 'KlPDUMerk'
    label = 'Merknamen PDU'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPDUMerk'
    definition = 'Lijst van merknamen van stroomverdelingssystemen (Power Distribution Unit) volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPDUMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

