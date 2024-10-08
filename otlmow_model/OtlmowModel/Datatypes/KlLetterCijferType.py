# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterCijferType(KeuzelijstField):
    """De mogelijke types van een individuele letter- of cijfermarkering."""
    naam = 'KlLetterCijferType'
    label = 'Type van de letter of het cijfer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterCijferType'
    definition = 'De mogelijke types van een individuele letter- of cijfermarkering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterCijferType'
    options = {
        'normaal---Cijfers-(basishoogte)': KeuzelijstWaarde(invulwaarde='normaal---Cijfers-(basishoogte)',
                                                            label='normaal - Cijfers (basishoogte)',
                                                            status='ingebruik',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Cijfers-(basishoogte)'),
        'normaal---Hoofdletters-(basishoogte)': KeuzelijstWaarde(invulwaarde='normaal---Hoofdletters-(basishoogte)',
                                                                 label='normaal - Hoofdletters (basishoogte)',
                                                                 status='ingebruik',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Hoofdletters-(basishoogte)'),
        'normaal---Kleine-letters-(basishoogte)': KeuzelijstWaarde(invulwaarde='normaal---Kleine-letters-(basishoogte)',
                                                                   label='normaal - Kleine letters (basishoogte)',
                                                                   status='ingebruik',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Kleine-letters-(basishoogte)'),
        'versmald---Cijfers-(4m-hoogte)': KeuzelijstWaarde(invulwaarde='versmald---Cijfers-(4m-hoogte)',
                                                           label='versmald - Cijfers (4m hoogte)',
                                                           status='ingebruik',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(4m-hoogte)'),
        'versmald---Cijfers-(6m-hoogte)': KeuzelijstWaarde(invulwaarde='versmald---Cijfers-(6m-hoogte)',
                                                           label='versmald - Cijfers (6m hoogte)',
                                                           status='ingebruik',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(6m-hoogte)'),
        'versmald---Cijfers-(basishoogte)': KeuzelijstWaarde(invulwaarde='versmald---Cijfers-(basishoogte)',
                                                             label='versmald - Cijfers (basishoogte)',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(basishoogte)'),
        'versmald---Hoofdletters-(4m-hoogte)': KeuzelijstWaarde(invulwaarde='versmald---Hoofdletters-(4m-hoogte)',
                                                                label='versmald - Hoofdletters (4m hoogte)',
                                                                status='ingebruik',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(4m-hoogte)'),
        'versmald---Hoofdletters-(6m-hoogte)': KeuzelijstWaarde(invulwaarde='versmald---Hoofdletters-(6m-hoogte)',
                                                                label='versmald - Hoofdletters (6m hoogte)',
                                                                status='ingebruik',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(6m-hoogte)'),
        'versmald---Hoofdletters-(basishoogte)': KeuzelijstWaarde(invulwaarde='versmald---Hoofdletters-(basishoogte)',
                                                                  label='versmald - Hoofdletters (basishoogte)',
                                                                  status='ingebruik',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(basishoogte)'),
        'versmald---Kleine-letters-(basishoogte)': KeuzelijstWaarde(invulwaarde='versmald---Kleine-letters-(basishoogte)',
                                                                    label='versmald - Kleine letters (basishoogte)',
                                                                    status='ingebruik',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Kleine-letters-(basishoogte)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

