# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPDUModelnaam(KeuzelijstField):
    """Lijst van modelnamen van stroomverdelingssystemen (Power Distribution Unit) volgens de fabrikant."""
    naam = 'KlPDUModelnaam'
    label = 'Modelnamen PDU'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPDUModelnaam'
    definition = 'Lijst van modelnamen van stroomverdelingssystemen (Power Distribution Unit) volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPDUModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

