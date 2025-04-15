# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriCommunicatieprotocolVerkeersdetectie(KeuzelijstField):
    """De mogelijke opties voor de communicatiewijze van een VRI verkeersdetectie."""
    naam = 'KlVriCommunicatieprotocolVerkeersdetectie'
    label = 'VRI communicatieprotocol verkeersdetectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriCommunicatieprotocolVerkeersdetectie'
    definition = 'De mogelijke opties voor de communicatiewijze van een VRI verkeersdetectie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriCommunicatieprotocolVerkeersdetectie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

