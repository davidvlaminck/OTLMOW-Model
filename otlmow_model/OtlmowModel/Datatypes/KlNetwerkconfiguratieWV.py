# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkconfiguratieWV(KeuzelijstField):
    """De mogelijke opties van de netwerkconfiguratie in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole inzake wegverlichting."""
    naam = 'KlNetwerkconfiguratieWV'
    label = 'Netwerkconfiguratie wegverlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkconfiguratieWV'
    definition = 'De mogelijke opties van de netwerkconfiguratie in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole inzake wegverlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkconfiguratieWV'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

