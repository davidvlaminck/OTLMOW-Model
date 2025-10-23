# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStandaardeenheid(KeuzelijstField):
    """TODO (Signalisatie Vlaanderen)."""
    naam = 'KlStandaardeenheid'
    label = 'Standaardeenheid'
    objectUri = 'https://data.vlaanderen.be/ns/projecten#KlStandaardeenheid'
    definition = 'TODO (Signalisatie Vlaanderen).'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://todo.com'
    options = {
        'None': KeuzelijstWaarde(invulwaarde='None',
                                 label='Code',
                                 status='ingebruik',
                                 definitie='TODO (Signalisatie Vlaanderen).',
                                 objectUri='https://todo.com')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

