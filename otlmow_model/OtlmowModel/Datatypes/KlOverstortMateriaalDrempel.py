# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverstortMateriaalDrempel(KeuzelijstField):
    """De materialen van vervaardiging van de overstort."""
    naam = 'KlOverstortMateriaalDrempel'
    label = 'Overstort materiaal drempel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortMateriaalDrempel'
    definition = 'De materialen van vervaardiging van de overstort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortMateriaalDrempel'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/beton'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='ingebruik',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortMateriaalDrempel/metselwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

