# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Radar."""
    naam = 'KlRadarMerk'
    label = 'Radar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarMerk'
    definition = 'Keuzelijst met merknamen voor Radar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarMerk'
    options = {
        'icoms': KeuzelijstWaarde(invulwaarde='icoms',
                                  label='ICOMS',
                                  status='ingebruik',
                                  definitie='ICOMS',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarMerk/icoms')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

