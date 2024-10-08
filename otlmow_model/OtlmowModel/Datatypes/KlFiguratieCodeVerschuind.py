# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieCodeVerschuind(KeuzelijstField):
    """Codes voor de verschuinde figuratie markering."""
    naam = 'KlFiguratieCodeVerschuind'
    label = 'Figuratie code verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCodeVerschuind'
    definition = 'Codes voor de verschuinde figuratie markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieCodeVerschuind'
    options = {
        'STOP-SmSc': KeuzelijstWaarde(invulwaarde='STOP-SmSc',
                                      label='STOP-SmSc',
                                      status='ingebruik',
                                      definitie='Een STOP markering smal en schuin.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/STOP-SmSc'),
        'VB-B1-GRsch': KeuzelijstWaarde(invulwaarde='VB-B1-GRsch',
                                        label='VB-B1-GRsch',
                                        status='ingebruik',
                                        definitie='Een omgekeerde driehoekmarkering groot en schuin.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/VB-B1-GRsch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

