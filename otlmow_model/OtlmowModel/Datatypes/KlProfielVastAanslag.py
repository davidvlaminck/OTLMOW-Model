# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlProfielVastAanslag(KeuzelijstField):
    """De mogelijke materialen van een aanslagprofiel."""
    naam = 'KlProfielVastAanslag'
    label = 'Materiaal aanslagprofiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlProfielVastAanslag'
    definition = 'De mogelijke materialen van een aanslagprofiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlProfielVastAanslag'
    options = {
        'constructiestaal': KeuzelijstWaarde(invulwaarde='constructiestaal',
                                             label='constructiestaal',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/constructiestaal'),
        'gietstaal': KeuzelijstWaarde(invulwaarde='gietstaal',
                                      label='gietstaal',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/gietstaal'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/hout'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='natuursteen',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/natuursteen'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/rvs'),
        'thermisch-verzinkt-staal': KeuzelijstWaarde(invulwaarde='thermisch-verzinkt-staal',
                                                     label='thermisch verzinkt staal',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielVastAanslag/thermisch-verzinkt-staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

