# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersspiegelVorm(KeuzelijstField):
    """De vormen van een verkeersspiegel."""
    naam = 'KlVerkeersspiegelVorm'
    label = 'Verkeersspiegel vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersspiegelVorm'
    definition = 'De vormen van een verkeersspiegel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersspiegelVorm'
    options = {
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='ingebruik',
                                        definitie='rechthoekige verkeersspiegel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rechthoekig'),
        'rond': KeuzelijstWaarde(invulwaarde='rond',
                                 label='rond',
                                 status='ingebruik',
                                 definitie='ronde verkeersspiegel',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersspiegelVorm/rond')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

