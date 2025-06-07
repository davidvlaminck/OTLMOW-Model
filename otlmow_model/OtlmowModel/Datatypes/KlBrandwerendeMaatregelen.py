# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandwerendeMaatregelen(KeuzelijstField):
    """Keuzelijst dat het brandwerenheidstype van de kokcercel terug geeft."""
    naam = 'KlBrandwerendeMaatregelen'
    label = 'Type brandwerendheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlBrandwerendeMaatregelen'
    definition = 'Keuzelijst dat het brandwerenheidstype van de kokcercel terug geeft.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandwerendeMaatregelen'
    options = {
        'brandwerende-bespuiting': KeuzelijstWaarde(invulwaarde='brandwerende-bespuiting',
                                                    label='brandwerende bespuiting',
                                                    status='ingebruik',
                                                    definitie='Brandwerende bespuiting',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandwerendeMaatregelen/brandwerende-bespuiting'),
        'brandwerende-deur': KeuzelijstWaarde(invulwaarde='brandwerende-deur',
                                              label='brandwerende deur ',
                                              status='ingebruik',
                                              definitie='Brandwerende deur ',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandwerendeMaatregelen/brandwerende-deur'),
        'brandwerende-dichtingen': KeuzelijstWaarde(invulwaarde='brandwerende-dichtingen',
                                                    label='brandwerende dichtingen ',
                                                    status='ingebruik',
                                                    definitie='Brandwerende dichtingen ',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandwerendeMaatregelen/brandwerende-dichtingen'),
        'brandwerende-platen': KeuzelijstWaarde(invulwaarde='brandwerende-platen',
                                                label='brandwerende platen',
                                                status='ingebruik',
                                                definitie='Brandwerende platen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandwerendeMaatregelen/brandwerende-platen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

