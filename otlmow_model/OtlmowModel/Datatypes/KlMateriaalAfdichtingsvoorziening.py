# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalAfdichtingsvoorziening(KeuzelijstField):
    """De mogelijke materialen waaruit een afdichtingsvoorziening bestaat."""
    naam = 'KlMateriaalAfdichtingsvoorziening'
    label = 'Materiaal afdichtingsvoorziening'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalAfdichtingsvoorziening'
    definition = 'De mogelijke materialen waaruit een afdichtingsvoorziening bestaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalAfdichtingsvoorziening'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichtingsvoorziening/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichtingsvoorziening/kunststof'),
        'rubber': KeuzelijstWaarde(invulwaarde='rubber',
                                   label='rubber',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichtingsvoorziening/rubber')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

