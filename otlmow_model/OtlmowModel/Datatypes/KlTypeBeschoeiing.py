# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBeschoeiing(KeuzelijstField):
    """Type beschoeiing."""
    naam = 'KlTypeBeschoeiing'
    label = 'Type beschoeiing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBeschoeiing'
    definition = 'Type beschoeiing.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeschoeiing'
    options = {
        'Berliner': KeuzelijstWaarde(invulwaarde='Berliner',
                                     label='Berliner',
                                     status='ingebruik',
                                     definitie='Berliner',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Berliner'),
        'Krings': KeuzelijstWaarde(invulwaarde='Krings',
                                   label='Krings',
                                   status='ingebruik',
                                   definitie='Krings',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschoeiing/Krings')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

