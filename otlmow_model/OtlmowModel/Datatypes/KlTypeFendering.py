# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeFendering(KeuzelijstField):
    """De keuzelijst die de verschillende types van fendering bevat."""
    naam = 'KlTypeFendering'
    label = 'Keuzelijst type fendering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeFendering'
    definition = 'De keuzelijst die de verschillende types van fendering bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeFendering'
    options = {
        'arch-(vb.-pi.-omega...)': KeuzelijstWaarde(invulwaarde='arch-(vb.-pi.-omega...)',
                                                    label='arch (vb. pi, omega,..)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/arch-(vb.-pi.-omega...)'),
        'cell': KeuzelijstWaarde(invulwaarde='cell',
                                 label='cell',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/cell'),
        'cone': KeuzelijstWaarde(invulwaarde='cone',
                                 label='cone',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/cone'),
        'drijfraam': KeuzelijstWaarde(invulwaarde='drijfraam',
                                      label='drijfraam',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/drijfraam'),
        'leg': KeuzelijstWaarde(invulwaarde='leg',
                                label='leg',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/leg'),
        'wielfender': KeuzelijstWaarde(invulwaarde='wielfender',
                                       label='wielfender',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeFendering/wielfender')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

