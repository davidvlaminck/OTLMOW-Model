# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorType(KeuzelijstField):
    """Het type van de neerslagsensor."""
    naam = 'KlNeerslagsensorType'
    label = 'Neerslagsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorType'
    definition = 'Het type van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorType'
    options = {
        'capacitief': KeuzelijstWaarde(invulwaarde='capacitief',
                                       label='capacitief',
                                       status='ingebruik',
                                       definitie='capacitief',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/capacitief'),
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/optisch'),
        'radar': KeuzelijstWaarde(invulwaarde='radar',
                                  label='radar',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/radar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

