# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpstelling(KeuzelijstField):
    """De opstellingen van de geluidswerende constructie."""
    naam = 'KlLEGCOpstelling'
    label = 'Opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpstelling'
    definition = 'De opstellingen van de geluidswerende constructie.'
    status = 'ingebruik'
    deprecated_version = '2.0.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpstelling'
    options = {
        'concaaf': KeuzelijstWaarde(invulwaarde='concaaf',
                                    label='concaaf',
                                    status='ingebruik',
                                    definitie='Concave opstelling t.o.v. de weg',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/concaaf'),
        'schuin-naar-achter-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-achter-hellend',
                                                       label='schuin naar achter hellend',
                                                       status='ingebruik',
                                                       definitie='schuin naar achter hellend t.o.v. de weg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-achter-hellend'),
        'schuin-naar-voor-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-voor-hellend',
                                                     label='schuin naar voor hellend',
                                                     status='ingebruik',
                                                     definitie='schuin naar voor hellend t.o.v. de weg',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/schuin-naar-voor-hellend'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='verticaal',
                                      status='ingebruik',
                                      definitie='verticaal t.o.v. de weg',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpstelling/verticaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

