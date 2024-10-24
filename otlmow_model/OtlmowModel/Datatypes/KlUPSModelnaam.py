# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSModelnaam(KeuzelijstField):
    """De modelnaam van de UPS."""
    naam = 'KlUPSModelnaam'
    label = 'UPS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSModelnaam'
    definition = 'De modelnaam van de UPS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSModelnaam'
    options = {
        'other': KeuzelijstWaarde(invulwaarde='other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Deze optie mag uitsluitend TIJDELIJK worden gebruikt en enkel tot de juiste gegevens beschikbaar zijn. Misbruik van deze optie leidt tot verminderde datakwaliteit.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/other'),
        'ps15': KeuzelijstWaarde(invulwaarde='ps15',
                                 label='PS15',
                                 status='ingebruik',
                                 definitie='PS15',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/ps15'),
        'quint4-ps-1ac-24dc-2-5-pt': KeuzelijstWaarde(invulwaarde='quint4-ps-1ac-24dc-2-5-pt',
                                                      label='QUINT4-PS-1AC-24DC-2.5-PT',
                                                      status='ingebruik',
                                                      definitie='QUINT4-PS-1AC-24DC-2.5-PT',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/quint4-ps-1ac-24dc-2-5-pt'),
        'smt750i': KeuzelijstWaarde(invulwaarde='smt750i',
                                    label='SMT750I',
                                    status='ingebruik',
                                    definitie='SMT750I',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/smt750i'),
        'smx1500rmi2u': KeuzelijstWaarde(invulwaarde='smx1500rmi2u',
                                         label='SMX1500RMI2U',
                                         status='ingebruik',
                                         definitie='SMX1500RMI2U',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/smx1500rmi2u'),
        'smx750i': KeuzelijstWaarde(invulwaarde='smx750i',
                                    label='SMX750I',
                                    status='ingebruik',
                                    definitie='SMX750I',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/smx750i'),
        'su1400rmxlib3u': KeuzelijstWaarde(invulwaarde='su1400rmxlib3u',
                                           label='SU1400RMXLIB3U',
                                           status='ingebruik',
                                           definitie='SU1400RMXLIB3U',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/su1400rmxlib3u'),
        'su750rm': KeuzelijstWaarde(invulwaarde='su750rm',
                                    label='SU750RM',
                                    status='ingebruik',
                                    definitie='SU750RM',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/su750rm'),
        'ub10-241': KeuzelijstWaarde(invulwaarde='ub10-241',
                                     label='UB10.241',
                                     status='ingebruik',
                                     definitie='UB10.241',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSModelnaam/ub10-241')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

