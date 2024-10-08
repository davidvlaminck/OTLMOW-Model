# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeDrempel(KeuzelijstField):
    """De keuzelijst die de verschillende type van drempels bevat."""
    naam = 'KlTypeDrempel'
    label = 'Keuzelijst type drempel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeDrempel'
    definition = 'De keuzelijst die de verschillende type van drempels bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeDrempel'
    options = {
        'gelijkliggende-drempel': KeuzelijstWaarde(invulwaarde='gelijkliggende-drempel',
                                                   label='gelijkliggende drempel',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeDrempel/gelijkliggende-drempel'),
        'opstande': KeuzelijstWaarde(invulwaarde='opstande',
                                     label='opstande',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeDrempel/opstande')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

