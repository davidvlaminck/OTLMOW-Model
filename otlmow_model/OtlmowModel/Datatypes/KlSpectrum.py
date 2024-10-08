# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpectrum(KeuzelijstField):
    """Mogelijke spectra"""
    naam = 'KlSpectrum'
    label = 'Spectrum'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpectrum'
    definition = 'Mogelijke spectra'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpectrum'
    options = {
        'dag': KeuzelijstWaarde(invulwaarde='dag',
                                label='Dag',
                                status='ingebruik',
                                definitie='Zichtbaar - dag',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpectrum/dag'),
        'dag-nacht': KeuzelijstWaarde(invulwaarde='dag-nacht',
                                      label='Dag/nacht',
                                      status='ingebruik',
                                      definitie='Zichtbaar - dag en nacht',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpectrum/dag-nacht'),
        'infrarood': KeuzelijstWaarde(invulwaarde='infrarood',
                                      label='Infrarood',
                                      status='ingebruik',
                                      definitie='Infrarood',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpectrum/infrarood'),
        'nacht': KeuzelijstWaarde(invulwaarde='nacht',
                                  label='Nacht',
                                  status='ingebruik',
                                  definitie='Zichtbaar - nacht',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpectrum/nacht')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

