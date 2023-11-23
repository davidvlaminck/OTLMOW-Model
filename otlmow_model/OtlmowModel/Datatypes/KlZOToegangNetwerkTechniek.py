# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZOToegangNetwerkTechniek(KeuzelijstField):
    """Keuzelijst die de technieken of standaarden waarmee signalen over het netwerk verstuurd worden, bevat."""
    naam = 'KlZOToegangNetwerkTechniek'
    label = 'Zender ontvanger toegang netwerk techniek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZOToegangNetwerkTechniek'
    definition = 'Keuzelijst die de technieken of standaarden waarmee signalen over het netwerk verstuurd worden, bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZOToegangNetwerkTechniek'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

