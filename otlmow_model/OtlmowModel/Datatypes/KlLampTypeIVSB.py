# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLampTypeIVSB(KeuzelijstField):
    """Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord."""
    naam = 'KlLampTypeIVSB'
    label = 'lamp type inwendig verlicht signalisatiebord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLampTypeIVSB'
    definition = 'Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLampTypeIVSB'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

