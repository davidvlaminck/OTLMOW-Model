# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor pompen."""
    naam = 'KlPompModelnaam'
    label = 'Typepomp modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompModelnaam'
    definition = 'Lijst met modelnamen voor pompen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompModelnaam'
    options = {
        '1sv22f011t': KeuzelijstWaarde(invulwaarde='1sv22f011t',
                                       label='1SV22F011T',
                                       status='ingebruik',
                                       definitie='1SV22F011T',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompModelnaam/1sv22f011t')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

