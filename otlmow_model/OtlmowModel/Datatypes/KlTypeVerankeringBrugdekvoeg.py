# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVerankeringBrugdekvoeg(KeuzelijstField):
    """Het type van de verankering van de brugdekvoeg."""
    naam = 'KlTypeVerankeringBrugdekvoeg'
    label = 'Type verankering brugdekvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVerankeringBrugdekvoeg'
    definition = 'Het type van de verankering van de brugdekvoeg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVerankeringBrugdekvoeg'
    options = {
        'type-2a': KeuzelijstWaarde(invulwaarde='type-2a',
                                    label='type 2a',
                                    status='ingebruik',
                                    definitie='Verankering met wapeningsstaal.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringBrugdekvoeg/type-2a'),
        'type-2b': KeuzelijstWaarde(invulwaarde='type-2b',
                                    label='type 2b',
                                    status='ingebruik',
                                    definitie='Verankering met bouten of deuvels.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringBrugdekvoeg/type-2b'),
        'type-2c': KeuzelijstWaarde(invulwaarde='type-2c',
                                    label='type 2c',
                                    status='ingebruik',
                                    definitie='Verankering door verlijming.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringBrugdekvoeg/type-2c'),
        'type-2d': KeuzelijstWaarde(invulwaarde='type-2d',
                                    label='type 2d',
                                    status='ingebruik',
                                    definitie='Verankering door combinatie verlijming ingeboorde wapening.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringBrugdekvoeg/type-2d')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

