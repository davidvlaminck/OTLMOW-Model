# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoofdtype(KeuzelijstField):
    """De mogelijke types hoofd van een constructiehoofd."""
    naam = 'KlHoofdtype'
    label = 'Hoofdtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHoofdtype'
    definition = 'De mogelijke types hoofd van een constructiehoofd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoofdtype'
    options = {
        '(afwaarts)benedenhoofd': KeuzelijstWaarde(invulwaarde='(afwaarts)benedenhoofd',
                                                   label='(afwaarts)benedenhoofd',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoofdtype/(afwaarts)benedenhoofd'),
        '(opwaarts)bovenhoofd': KeuzelijstWaarde(invulwaarde='(opwaarts)bovenhoofd',
                                                 label='(opwaarts)bovenhoofd',
                                                 status='ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoofdtype/(opwaarts)bovenhoofd'),
        'middenhoofd': KeuzelijstWaarde(invulwaarde='middenhoofd',
                                        label='middenhoofd',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHoofdtype/middenhoofd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

