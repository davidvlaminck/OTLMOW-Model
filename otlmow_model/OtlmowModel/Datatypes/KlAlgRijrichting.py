# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgRijrichting(KeuzelijstField):
    """De mogelijke rijrichtingen."""
    naam = 'KlAlgRijrichting'
    label = 'Rijrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgRijrichting'
    definition = 'De mogelijke rijrichtingen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgRijrichting'
    options = {
        'aflopend': KeuzelijstWaarde(invulwaarde='aflopend',
                                     label='aflopend',
                                     status='ingebruik',
                                     definitie='Aflopende rijrichting.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/aflopend'),
        'dubbele-rijrichting': KeuzelijstWaarde(invulwaarde='dubbele-rijrichting',
                                                label='dubbele rijrichting',
                                                status='ingebruik',
                                                definitie='Dubbele rijrichting.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/dubbele-rijrichting'),
        'oplopend': KeuzelijstWaarde(invulwaarde='oplopend',
                                     label='oplopend',
                                     status='ingebruik',
                                     definitie='Oplopende rijrichting.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijrichting/oplopend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

