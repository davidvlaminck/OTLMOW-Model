# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAantalLampenIVSB(KeuzelijstField):
    """Het aantal lampen dat aanwezig is in het inwendig verlicht signalisatiebord."""
    naam = 'KlAantalLampenIVSB'
    label = 'aantal lampen inwendig verlicht signalisatiebord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAantalLampenIVSB'
    definition = 'Het aantal lampen dat aanwezig is in het inwendig verlicht signalisatiebord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAantalLampenIVSB'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

