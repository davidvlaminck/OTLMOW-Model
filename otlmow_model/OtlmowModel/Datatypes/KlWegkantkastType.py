# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegkantkastType(KeuzelijstField):
    """Keuzelijst voor gangbare types voor wegkantkasten."""
    naam = 'KlWegkantkastType'
    label = 'Wegkantkast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegkantkastType'
    definition = 'Keuzelijst voor gangbare types voor wegkantkasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegkantkastType'
    options = {
        'A': KeuzelijstWaarde(invulwaarde='A',
                              label='A',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/A'),
        'D': KeuzelijstWaarde(invulwaarde='D',
                              label='D',
                              status='ingebruik',
                              definitie='Wegkantkast type D',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/D'),
        'DD': KeuzelijstWaarde(invulwaarde='DD',
                               label='DD',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/DD'),
        'E': KeuzelijstWaarde(invulwaarde='E',
                              label='E',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/E'),
        'F': KeuzelijstWaarde(invulwaarde='F',
                              label='F',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegkantkastType/F')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

