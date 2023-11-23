# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRasterMazen(KeuzelijstField):
    """Types van de mazen in het ecoraster."""
    naam = 'KlRasterMazen'
    label = 'Rastermazen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRasterMazen'
    definition = 'Types van de mazen in het ecoraster.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRasterMazen'
    options = {
        'fijnmazig': KeuzelijstWaarde(invulwaarde='fijnmazig',
                                      label='fijnmazig',
                                      status='ingebruik',
                                      definitie='Een fijnmazig raster.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/fijnmazig'),
        'grofmazig': KeuzelijstWaarde(invulwaarde='grofmazig',
                                      label='grofmazig',
                                      status='ingebruik',
                                      definitie='Een grofmazig raster.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRasterMazen/grofmazig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

