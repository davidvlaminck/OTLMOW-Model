# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterVerschaaldType(KeuzelijstField):
    """De mogelijke types van een individueel verschaalde lettermarkering."""
    naam = 'KlLetterVerschaaldType'
    label = 'Type van de verschaalde letter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterVerschaaldType'
    definition = 'De mogelijke types van een individueel verschaalde lettermarkering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterVerschaaldType'
    options = {
        'versmald---Hoofdletters-(basishoogte-0.4-meter)': KeuzelijstWaarde(invulwaarde='versmald---Hoofdletters-(basishoogte-0.4-meter)',
                                                                            label='versmald - Hoofdletters (basishoogte 0.4 meter)',
                                                                            status='ingebruik',
                                                                            definitie='Versmalde hoofdletters bij verschaling (basishoogte 0.4 meter)',
                                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaaldType/versmald---Hoofdletters-(basishoogte-0.4-meter)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

