# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompMerk(KeuzelijstField):
    """Lijst met merknamen voor pompen."""
    naam = 'KlPompMerk'
    label = 'Typepomp merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPompMerk'
    definition = 'Lijst met merknamen voor pompen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompMerk'
    options = {
        'lowara': KeuzelijstWaarde(invulwaarde='lowara',
                                   label='Lowara',
                                   status='ingebruik',
                                   definitie='LOWARA',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompMerk/lowara'),
        'xylem': KeuzelijstWaarde(invulwaarde='xylem',
                                  label='Xylem',
                                  status='ingebruik',
                                  definitie='Xylem',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompMerk/xylem')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

