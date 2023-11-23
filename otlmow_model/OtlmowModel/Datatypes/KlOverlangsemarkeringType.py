# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverlangsemarkeringType(KeuzelijstField):
    """Mogelijke types van de overlangse markering."""
    naam = 'KlOverlangsemarkeringType'
    label = 'Overlangse markering type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverlangsemarkeringType'
    definition = 'Mogelijke types van de overlangse markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverlangsemarkeringType'
    options = {
        'doorlopend': KeuzelijstWaarde(invulwaarde='doorlopend',
                                       label='doorlopend',
                                       status='ingebruik',
                                       definitie='Een overlangse markering bestaande uit een doorlopende streep.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/doorlopend'),
        'onderbroken': KeuzelijstWaarde(invulwaarde='onderbroken',
                                        label='onderbroken',
                                        status='ingebruik',
                                        definitie='Een overlangse markering bestaande uit een onderbroken streep.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverlangsemarkeringType/onderbroken')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

