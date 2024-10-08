# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgInspecteerbaarheid(KeuzelijstField):
    """De mogelijke opties van inspecteerbaarheid."""
    naam = 'KlAlgInspecteerbaarheid'
    label = 'Inspecteerbaarheid van een element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgInspecteerbaarheid'
    definition = 'De mogelijke opties van inspecteerbaarheid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgInspecteerbaarheid'
    options = {
        'gedeeltelijk': KeuzelijstWaarde(invulwaarde='gedeeltelijk',
                                         label='gedeeltelijk',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgInspecteerbaarheid/gedeeltelijk'),
        'ja': KeuzelijstWaarde(invulwaarde='ja',
                               label='ja',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgInspecteerbaarheid/ja'),
        'nee': KeuzelijstWaarde(invulwaarde='nee',
                                label='nee',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgInspecteerbaarheid/nee'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgInspecteerbaarheid/onbekend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

