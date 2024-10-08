# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioTransportType(KeuzelijstField):
    """Lijst met mogelijke types voor transport van audio over een medium."""
    naam = 'KlAudioTransportType'
    label = 'Audio transport type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioTransportType'
    definition = 'Lijst met mogelijke types voor transport van audio over een medium.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioTransportType'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/analoog'),
        'voip': KeuzelijstWaarde(invulwaarde='voip',
                                 label='voip',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioTransportType/voip')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

