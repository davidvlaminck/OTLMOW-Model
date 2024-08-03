# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPenetratiegraad(KeuzelijstField):
    """De graad van penetratie."""
    naam = 'KlPenetratiegraad'
    label = 'Penetratiegraad'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPenetratiegraad'
    definition = 'De graad van penetratie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPenetratiegraad'
    options = {
        'half-gepenetreerd': KeuzelijstWaarde(invulwaarde='half-gepenetreerd',
                                              label='half gepenetreerd',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPenetratiegraad/half-gepenetreerd'),
        'vol-en-zat-genepetreerd': KeuzelijstWaarde(invulwaarde='vol-en-zat-genepetreerd',
                                                    label='vol en zat genepetreerd',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPenetratiegraad/vol-en-zat-genepetreerd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

