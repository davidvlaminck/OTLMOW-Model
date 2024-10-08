# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerMerk(KeuzelijstField):
    """Het merk van de omvormer."""
    naam = 'KlOmvormerMerk'
    label = 'Omvormer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerMerk'
    definition = 'Het merk van de omvormer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerMerk'
    options = {
        'axis': KeuzelijstWaarde(invulwaarde='axis',
                                 label='Axis',
                                 status='ingebruik',
                                 definitie='Axis',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/axis'),
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/bosch'),
        'c4line': KeuzelijstWaarde(invulwaarde='c4line',
                                   label='C4LINE',
                                   status='ingebruik',
                                   definitie='C4LINE',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/c4line'),
        'kti-networks': KeuzelijstWaarde(invulwaarde='kti-networks',
                                         label='KTI NETWORKS',
                                         status='ingebruik',
                                         definitie='KTI NETWORKS',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/kti-networks'),
        'nvt-phybridge': KeuzelijstWaarde(invulwaarde='nvt-phybridge',
                                          label='NVT Phybridge',
                                          status='ingebruik',
                                          definitie='NVT Phybridge',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/nvt-phybridge'),
        'siqura': KeuzelijstWaarde(invulwaarde='siqura',
                                   label='Siqura',
                                   status='ingebruik',
                                   definitie='Siqura',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerMerk/siqura')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

