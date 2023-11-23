# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtsensorMerk(KeuzelijstField):
    """Lichtsensor merken."""
    naam = 'KlLichtsensorMerk'
    label = 'Lichtsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtsensorMerk'
    definition = 'Lichtsensor merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtsensorMerk'
    options = {
        'schreder': KeuzelijstWaarde(invulwaarde='schreder',
                                     label='Schreder',
                                     status='ingebruik',
                                     definitie='Schreder',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorMerk/schreder')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

